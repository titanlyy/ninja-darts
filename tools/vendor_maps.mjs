import { copyFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { build } from 'esbuild';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
// Classic workers work in opaque preview origins where module workers do not.
// Bundle the same audited v6 code, rather than downgrading the map library.
await build({
  entryPoints: [path.join(root, 'node_modules/maplibre-gl/dist/maplibre-gl-worker.mjs')],
  outfile: path.join(root, 'vendor/maplibre-gl-worker-6.16.0.cjs'),
  bundle: true,
  format: 'iife',
  platform: 'browser',
  target: 'es2020',
  minify: true,
  legalComments: 'inline',
});
for (const name of ['maplibre-gl.mjs', 'maplibre-gl-shared.mjs', 'maplibre-gl-worker.mjs', 'maplibre-gl.css']) {
  await copyFile(path.join(root, 'node_modules/maplibre-gl/dist', name), path.join(root, 'vendor', name));
}
for (const [source, target] of [
  ['maplibre-gl/LICENSE.txt', 'maplibre-gl.LICENSE.txt'],
  ['@maplibre/maplibre-gl-leaflet/leaflet-maplibre-gl.js', 'leaflet-maplibre-gl.js'],
  ['@maplibre/maplibre-gl-leaflet/LICENSE', 'leaflet-maplibre-gl.LICENSE.txt'],
]) {
  await copyFile(path.join(root, 'node_modules', source), path.join(root, 'vendor', target));
}
console.log('Vendored pinned preview map libraries and licenses.');
