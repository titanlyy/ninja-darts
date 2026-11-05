import { cp, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const target = path.join(root, 'www');
// An explicit allowlist keeps git metadata, tools, caches and local configuration
// out of both web deployments and future Capacitor packages.
export const publicAssets = [
  'index.html', 'css', 'js', 'data', 'icons', 'vendor',
  'manifest.webmanifest', 'sw.js', '.nojekyll',
];
await rm(target, { recursive: true, force: true });
await mkdir(target, { recursive: true });
for (const asset of publicAssets) {
  await cp(path.join(root, asset), path.join(target, asset), { recursive: true });
}
console.log(`Public web/native bundle: ${target}`);
