import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const outputPath = resolve(__dirname, '../_data/analytics-snapshot.json');

const siteUrl = (process.env.GOATCOUNTER_SITE_URL || 'https://yulong.goatcounter.com').replace(/\/+$/, '');
const apiToken = (process.env.GOATCOUNTER_API_TOKEN || '').trim();

const fallbackSnapshot = {
  connected: false,
  siteUrl,
  generatedAt: null,
  periodLabel: 'All time',
  totalVisitors: null,
  countries: []
};

const getCountryFlag = (code) => {
  const normalized = (code || '').trim().toUpperCase();
  if (!/^[A-Z]{2}$/.test(normalized)) return '';

  return [...normalized]
    .map((letter) => String.fromCodePoint(letter.charCodeAt(0) + 127397))
    .join('');
};

async function writeSnapshot(data) {
  await mkdir(dirname(outputPath), { recursive: true });
  await writeFile(outputPath, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

async function apiGet(path, params = {}) {
  const url = new URL(`/api/v0/${path}`, siteUrl);
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== null && value !== '') {
      url.searchParams.set(key, value);
    }
  }

  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiToken}`
    }
  });

  if (!response.ok) {
    throw new Error(`GoatCounter request failed: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

async function main() {
  if (!apiToken) {
    await writeSnapshot(fallbackSnapshot);
    console.warn('GoatCounter snapshot skipped: GOATCOUNTER_API_TOKEN is not set.');
    return;
  }

  try {
    const sitesResponse = await apiGet('sites');
    const code = new URL(siteUrl).hostname.split('.')[0];
    const site =
      sitesResponse.sites?.find((entry) => entry.code === code) ?? sitesResponse.sites?.[0] ?? null;
    const start = site?.first_hit_at || site?.created_at || '2024-01-01T00:00:00Z';
    const end = new Date().toISOString();

    const [totalResponse, locationsResponse] = await Promise.all([
      apiGet('stats/total', { start, end }),
      apiGet('stats/locations', { start, end, limit: '100' })
    ]);

    await writeSnapshot({
      connected: true,
      siteUrl,
      generatedAt: end,
      periodLabel: 'All time',
      totalVisitors: totalResponse.total ?? 0,
      countries: (locationsResponse.stats || []).map((item) => ({
        code: item.id || '',
        name: item.name || 'Unknown',
        count: item.count || 0,
        flag: getCountryFlag(item.id || '')
      }))
    });

    console.log('GoatCounter snapshot updated.');
  } catch (error) {
    await writeSnapshot(fallbackSnapshot);
    console.error(`GoatCounter snapshot failed: ${error instanceof Error ? error.message : String(error)}`);
  }
}

await main();
