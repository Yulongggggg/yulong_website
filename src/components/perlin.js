// src/components/perlin.js
// 一个基于单文件的简单 Perlin 噪声实现

function makeNoise2D(seed = 1) {
	const P = [];
	const hash = function (seed) {
		let x = Math.sin(seed++) * 10000;
		return x - Math.floor(x);
	};
	for (let i = 0; i < 256; i++) {
		P[i] = Math.floor(hash(seed + i) * 256);
	}
	const perm = [];
	for (let i = 0; i < 512; i++) {
		perm[i] = P[i & 255];
	}

	const fade = function (t) {
		return t * t * t * (t * (t * 6 - 15) + 10);
	};
	const lerp = function (a, b, t) {
		return a + (b - a) * t;
	};
	const grad2D = function (hash, x, y) {
		const v = hash & 3;
		if (v === 0) return x + y;
		if (v === 1) return -x + y;
		if (v === 2) return x - y;
		return -x - y;
	};

	return function (x, y) {
		const X = Math.floor(x) & 255;
		const Y = Math.floor(y) & 255;
		x -= Math.floor(x);
		y -= Math.floor(y);
		const u = fade(x);
		const v = fade(y);
		const A = perm[X] + Y,
			AA = perm[A],
			AB = perm[A + 1],
			B = perm[X + 1] + Y,
			BA = perm[B],
			BB = perm[B + 1];

		return lerp(v, lerp(u, grad2D(perm[AA], x, y), grad2D(perm[BA], x - 1, y)), lerp(u, grad2D(perm[AB], x, y - 1), grad2D(perm[BB], x - 1, y - 1)));
	};
}

export { makeNoise2D };
