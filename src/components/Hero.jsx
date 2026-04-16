import { createSignal, onCleanup, onMount } from 'solid-js';
import { makeNoise2D } from './perlin.js';

const PAPER = '#f5f0e4';
const HERO_FONT =
	'"Merriweather", "Georgia", "Palatino Linotype", serif';
const PALETTE = ['#9eb9d7', '#adc4de', '#b9cde1', '#b7cda0', '#c7b5d9', '#d5cb9d'];

function clamp(value, min, max) {
	return Math.min(max, Math.max(min, value));
}

function hexToRgb(hex) {
	const raw = hex.replace('#', '');
	return {
		r: parseInt(raw.slice(0, 2), 16),
		g: parseInt(raw.slice(2, 4), 16),
		b: parseInt(raw.slice(4, 6), 16)
	};
}

function mixChannel(a, b, t) {
	return Math.round(a + (b - a) * t);
}

function mixColor(a, b, t) {
	return {
		r: mixChannel(a.r, b.r, t),
		g: mixChannel(a.g, b.g, t),
		b: mixChannel(a.b, b.b, t)
	};
}

function toRgba(color, alpha) {
	return `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha})`;
}

function measureTrackedText(ctx, value, tracking) {
	return value.split('').reduce((width, letter, index) => {
		return width + ctx.measureText(letter).width + (index === value.length - 1 ? 0 : tracking);
	}, 0);
}

function drawTrackedText(ctx, value, centerX, centerY, tracking) {
	let cursor = centerX - measureTrackedText(ctx, value, tracking) / 2;
	for (const letter of value) {
		ctx.fillText(letter, cursor, centerY);
		cursor += ctx.measureText(letter).width + tracking;
	}
}

function drawTrackedStroke(ctx, value, centerX, centerY, tracking) {
	let cursor = centerX - measureTrackedText(ctx, value, tracking) / 2;
	for (const letter of value) {
		ctx.strokeText(letter, cursor, centerY);
		cursor += ctx.measureText(letter).width + tracking;
	}
}

export default function Hero(props) {
	let canvasRef;

	const [isFading, setIsFading] = createSignal(false);
	const [isExited, setIsExited] = createSignal(false);

	let frameId = 0;
	let enterTimeoutId = 0;
	let restoreOverflow = '';

	const text = () => (props.text?.trim() || 'YULONG LIU').toUpperCase();
	const prefix = () => props.prefix?.trim() || "Hi, I'm";
	const subtitle = () =>
		props.subtitle?.trim() || 'Ph.D. student in Earth Sciences at Cornell University';

	const handleEnter = () => {
		if (isFading() || isExited()) {
			return;
		}

		setIsFading(true);
		document.body.style.overflow = restoreOverflow;

		enterTimeoutId = window.setTimeout(() => {
			setIsExited(true);
			cancelAnimationFrame(frameId);
		}, 760);
	};

		onMount(() => {
			const canvas = canvasRef;
			const ctx = canvas?.getContext('2d', { alpha: false });

		if (!canvas || !ctx) {
			return;
		}

		restoreOverflow = document.body.style.overflow;
		document.body.style.overflow = 'hidden';

		let disposed = false;
		let width = window.innerWidth;
		let height = window.innerHeight;
		let dpr = Math.min(window.devicePixelRatio || 1, 2);
			let elapsed = 0;
			let lastTime = performance.now();
			let particles = [];
			let typeMetrics = null;
			const MOBILE_BREAKPOINT = 720;

			const palette = PALETTE.map(hexToRgb);
		const colorNoise = makeNoise2D(19);
		const driftNoise = makeNoise2D(71);
		const depthNoise = makeNoise2D(131);
		const splashNoise = makeNoise2D(211);
		const textCanvas = document.createElement('canvas');
		const textCtx = textCanvas.getContext('2d', { willReadFrequently: true });
		const pointer = {
			x: width * 0.5,
			y: height * 0.52,
			radius: 170,
			active: false
		};

			if (!textCtx) {
				document.body.style.overflow = restoreOverflow;
				return;
			}

			const isMobile = () => width < MOBILE_BREAKPOINT;

		class Particle {
			constructor(x, y, color, radius, alpha, depth, roam) {
				this.homeX = x;
				this.homeY = y;
				this.x = x + (Math.random() - 0.5) * width * roam;
				this.y = y + (Math.random() - 0.5) * height * roam;
				this.vx = (Math.random() - 0.5) * 1.3;
				this.vy = (Math.random() - 0.5) * 1.3;
				this.radius = radius;
				this.alpha = alpha;
				this.color = color;
				this.depth = depth;
				this.seed = Math.random() * 1000;
			}

			update(time) {
				const swayX = driftNoise(this.seed, time * 0.000065 + this.seed) * (0.7 + this.depth * 1.2);
				const swayY =
					driftNoise(this.seed + 33, time * 0.00007 + this.seed) * (0.62 + this.depth * 1.05);
				const targetX = this.homeX + swayX;
				const targetY = this.homeY + swayY;

				this.vx += (targetX - this.x) * 0.092;
				this.vy += (targetY - this.y) * 0.092;

				if (pointer.active) {
					const dx = this.x - pointer.x;
					const dy = this.y - pointer.y;
					const distance = Math.sqrt(dx * dx + dy * dy) || 0.001;

					if (distance < pointer.radius) {
						const force = ((pointer.radius - distance) / pointer.radius) ** 2;
						this.vx += (dx / distance) * force * (6.4 + this.depth * 2.4);
						this.vy += (dy / distance) * force * (6.4 + this.depth * 2.4);
					}
				}

				this.vx *= 0.89;
				this.vy *= 0.89;
				this.x += this.vx;
				this.y += this.vy;
			}

			draw() {
				const bloom = this.radius * (2.6 + this.depth * 0.5);
				const gradient = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, bloom);
				gradient.addColorStop(0, toRgba(this.color, this.alpha));
				gradient.addColorStop(0.58, toRgba(this.color, this.alpha * 0.22));
				gradient.addColorStop(1, toRgba(this.color, 0));

				ctx.fillStyle = gradient;
				ctx.beginPath();
				ctx.arc(this.x, this.y, bloom, 0, Math.PI * 2);
				ctx.fill();

				ctx.fillStyle = toRgba(this.color, Math.min(0.46, this.alpha * 1.2));
				ctx.beginPath();
				ctx.arc(this.x, this.y, this.radius * 0.96, 0, Math.PI * 2);
				ctx.fill();
			}
		}

		const resizeCanvas = () => {
			width = window.innerWidth;
			height = window.innerHeight;
			dpr = Math.min(window.devicePixelRatio || 1, 2);

			canvas.width = Math.floor(width * dpr);
			canvas.height = Math.floor(height * dpr);
			canvas.style.width = `${width}px`;
			canvas.style.height = `${height}px`;
			ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

			textCanvas.width = width;
			textCanvas.height = height;
		};

			const pickTypeMetrics = () => {
				const letters = text().replace(/\s+/g, '').length || 8;

				let fontSize = isMobile()
					? Math.min(width / (letters * 0.17), height * 0.16)
					: Math.min(width / (letters * 0.245), height * 0.34);

				fontSize = isMobile()
					? clamp(fontSize, 56, 104)
					: clamp(fontSize, 136, 286);

				let tracking = isMobile()
					? fontSize * -0.003
					: fontSize * -0.0015;

				textCtx.font = `900 ${fontSize}px ${HERO_FONT}`;

				while (
					measureTrackedText(textCtx, text(), tracking) > (isMobile() ? width * 0.9 : width * 0.9) &&
					fontSize > (isMobile() ? 60 : 112)
				) {
					fontSize -= isMobile() ? 2 : 4;
					tracking = isMobile()
						? fontSize * -0.0025
						: fontSize * -0.0013;
					textCtx.font = `900 ${fontSize}px ${HERO_FONT}`;
				}

				return {
					fontSize,
					tracking,
					baseline: isMobile() ? height * 0.5 : height * 0.54
				};
			};

		const sampleColor = (x, y) => {
			const nx = x / width;
			const ny = y / height;
			const blend = clamp((colorNoise(nx * 2 + 4, ny * 1.8 + 1.5) + 1) / 2, 0, 0.999);
			const depth = clamp((depthNoise(nx * 3.2 + 10, ny * 2.8 + 4) + 1) / 2, 0, 1);
			const slot = blend * (palette.length - 1);
			const a = Math.floor(slot);
			const b = Math.min(a + 1, palette.length - 1);
			const tone = mixColor(palette[a], palette[b], slot - a);
			const lift = 0.96 + depth * 0.08;

			return {
				color: {
					r: clamp(Math.round(tone.r * lift), 0, 255),
					g: clamp(Math.round(tone.g * lift), 0, 255),
					b: clamp(Math.round(tone.b * lift), 0, 255)
				},
				depth
			};
		};

		const buildParticles = () => {
			resizeCanvas();
			textCtx.clearRect(0, 0, width, height);
			textCtx.fillStyle = '#111';
			textCtx.textAlign = 'left';
			textCtx.textBaseline = 'middle';

			typeMetrics = pickTypeMetrics();
			textCtx.font = `900 ${typeMetrics.fontSize}px ${HERO_FONT}`;
			drawTrackedText(textCtx, text(), width / 2, typeMetrics.baseline, typeMetrics.tracking);

			const image = textCtx.getImageData(0, 0, width, height).data;
				const step = isMobile() ? 3 : 4;
			const nextParticles = [];

			for (let y = 0; y < height; y += step) {
				for (let x = 0; x < width; x += step) {
					const alpha = image[(y * width + x) * 4 + 3];
					if (alpha < 34) {
						continue;
					}

					const { color, depth } = sampleColor(x, y);
					const splash = clamp((splashNoise(x * 0.022, y * 0.024) + 1) / 2, 0, 1);
						const baseRadius = isMobile()
							? 2.7 + Math.random() * 1.5 + depth * 0.6 + splash * 0.32
							: 3.4 + Math.random() * 2.1 + depth * 0.9 + splash * 0.52;
						const baseAlpha = isMobile()
							? 0.18 + Math.random() * 0.12 + depth * 0.04
							: 0.16 + Math.random() * 0.11 + depth * 0.05;

					nextParticles.push(
						new Particle(
							x + (Math.random() - 0.5) * 0.7,
							y + (Math.random() - 0.5) * 0.7,
							color,
							baseRadius,
							baseAlpha,
							depth,
							0.035
						)
					);

					if (Math.random() < 0.64) {
						nextParticles.push(
							new Particle(
								x + (Math.random() - 0.5) * 10,
								y + (Math.random() - 0.5) * 10,
								color,
								baseRadius * (0.78 + Math.random() * 0.48),
								baseAlpha * 0.92,
								depth,
								0.045
							)
						);
					}

					if (Math.random() < 0.16) {
						nextParticles.push(
							new Particle(
								x + (Math.random() - 0.5) * 16,
								y + (Math.random() - 0.5) * 16,
								color,
								baseRadius * (1.18 + Math.random() * 0.65),
								baseAlpha * 0.72,
								depth,
								0.06
							)
						);
					}
				}
			}

			particles = nextParticles;
			pointer.x = width * 0.5;
			pointer.y = height * 0.52;
		};

		const drawBackdrop = () => {
			ctx.fillStyle = PAPER;
			ctx.fillRect(0, 0, width, height);

			const washes = [
				{ x: width * 0.14, y: height * 0.16, radius: width * 0.18, color: 'rgba(206, 210, 182, 0.16)' },
				{ x: width * 0.46, y: height * 0.44, radius: width * 0.18, color: 'rgba(187, 201, 219, 0.11)' },
				{ x: width * 0.82, y: height * 0.24, radius: width * 0.17, color: 'rgba(204, 191, 214, 0.11)' },
				{ x: width * 0.72, y: height * 0.78, radius: width * 0.2, color: 'rgba(197, 212, 189, 0.08)' }
			];

			for (const wash of washes) {
				const gradient = ctx.createRadialGradient(wash.x, wash.y, 0, wash.x, wash.y, wash.radius);
				gradient.addColorStop(0, wash.color);
				gradient.addColorStop(1, 'rgba(255, 255, 255, 0)');
				ctx.fillStyle = gradient;
				ctx.fillRect(wash.x - wash.radius, wash.y - wash.radius, wash.radius * 2, wash.radius * 2);
			}
		};

		const drawGhostText = () => {
			if (!typeMetrics) {
				return;
			}

			const fill = ctx.createLinearGradient(width * 0.1, height * 0.42, width * 0.9, height * 0.62);
			fill.addColorStop(0, 'rgba(155, 182, 208, 0.24)');
			fill.addColorStop(0.28, 'rgba(180, 205, 161, 0.21)');
			fill.addColorStop(0.62, 'rgba(193, 176, 217, 0.21)');
			fill.addColorStop(1, 'rgba(159, 194, 186, 0.21)');

			ctx.save();
			ctx.textAlign = 'left';
			ctx.textBaseline = 'middle';
			ctx.font = `900 ${typeMetrics.fontSize}px ${HERO_FONT}`;
			ctx.strokeStyle = 'rgba(118, 142, 161, 0.13)';
			ctx.lineWidth = Math.max(1.2, typeMetrics.fontSize * 0.0048);
			drawTrackedStroke(ctx, text(), width / 2, typeMetrics.baseline, typeMetrics.tracking);
			ctx.fillStyle = fill;
			drawTrackedText(ctx, text(), width / 2, typeMetrics.baseline, typeMetrics.tracking);
			ctx.restore();
		};

		const render = (now) => {
			elapsed += now - lastTime;
			lastTime = now;

			drawBackdrop();
			drawGhostText();

			for (const particle of particles) {
				particle.update(elapsed);
				particle.draw();
			}

			frameId = requestAnimationFrame(render);
		};

		const handlePointerMove = (event) => {
			pointer.active = true;
			pointer.x = event.clientX;
			pointer.y = event.clientY;
		};

		const handlePointerLeave = () => {
			pointer.active = false;
		};

		const handleResize = () => {
			buildParticles();
		};

		const start = async () => {
			if (document.fonts?.load) {
				try {
					await Promise.all([
						document.fonts.ready,
						document.fonts.load('900 240px "Merriweather"'),
						document.fonts.load('500 30px "Newsreader"'),
						document.fonts.load('600 18px "Manrope"')
					]);
				} catch {
					// Fall back gracefully when web fonts are unavailable.
				}
			}

			if (disposed) {
				return;
			}

			buildParticles();
			lastTime = performance.now();
			frameId = requestAnimationFrame(render);

			window.addEventListener('pointermove', handlePointerMove, { passive: true });
			canvas.addEventListener('pointerleave', handlePointerLeave);
			window.addEventListener('blur', handlePointerLeave);
			window.addEventListener('resize', handleResize);
		};

		start();

		onCleanup(() => {
			disposed = true;
			cancelAnimationFrame(frameId);
			window.clearTimeout(enterTimeoutId);
			window.removeEventListener('pointermove', handlePointerMove);
			canvas.removeEventListener('pointerleave', handlePointerLeave);
			window.removeEventListener('blur', handlePointerLeave);
			window.removeEventListener('resize', handleResize);
			document.body.style.overflow = restoreOverflow;
		});
	});

	return (
		<div
			class="hero-cover"
			onClick={handleEnter}
			role="button"
			tabIndex={0}
			onKeyDown={(event) => {
				if (event.key === 'Enter' || event.key === ' ') {
					event.preventDefault();
					handleEnter();
				}
			}}
			style={{
				display: isExited() ? 'none' : 'block',
				opacity: isFading() ? 0 : 1
			}}
			aria-label="Enter the site"
		>
			<canvas ref={canvasRef} class="hero-cover__canvas" />
			<div class="hero-cover__prefix">{prefix()}</div>
			<div class="hero-cover__subtitle">{subtitle()}</div>
			<div class="hero-cover__enter">click anywhere to enter</div>
			<style>{`
				.hero-cover {
					position: fixed;
					inset: 0;
					z-index: 999;
					background: ${PAPER};
					cursor: pointer;
					transition: opacity 760ms ease;
				}

				.hero-cover__canvas,
				.hero-cover__prefix,
				.hero-cover__subtitle,
				.hero-cover__enter {
					position: absolute;
					left: 50%;
					transform: translateX(-50%);
				}

				.hero-cover__canvas {
					inset: 0;
					transform: none;
					display: block;
					width: 100%;
					height: 100%;
				}

				.hero-cover__prefix,
				.hero-cover__subtitle,
				.hero-cover__enter {
					pointer-events: none;
					text-align: center;
				}

				.hero-cover__prefix {
					top: clamp(70px, 10vh, 132px);
					font-family: "Newsreader", "Iowan Old Style", serif;
					font-size: clamp(2rem, 2.6vw, 2.8rem);
					font-style: italic;
					letter-spacing: 0.02em;
					color: rgba(35, 49, 58, 0.8);
				}

				.hero-cover__subtitle {
					bottom: clamp(116px, 15vh, 176px);
					width: min(94vw, 1000px);
					font-family: "Manrope", "Helvetica Neue", sans-serif;
					font-size: clamp(1.06rem, 1.24vw, 1.22rem);
					letter-spacing: 0.22em;
					text-transform: uppercase;
					color: rgba(35, 49, 58, 0.64);
				}

				.hero-cover__enter {
					bottom: 44px;
					font-family: "Manrope", "Helvetica Neue", sans-serif;
					font-size: 0.92rem;
					letter-spacing: 0.18em;
					text-transform: uppercase;
					color: rgba(35, 49, 58, 0.7);
				}

				@media (max-width: 720px) {
					.hero-cover__prefix {
						top: 12vh;
						font-size: 1.6rem;
					}

					.hero-cover__subtitle {
						bottom: 96px;
						width: 88vw;
						font-size: 0.84rem;
						letter-spacing: 0.12em;
					}
				}
			`}</style>
		</div>
	);
}
