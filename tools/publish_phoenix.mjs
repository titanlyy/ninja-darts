// GitHub Actions only. Commit generated facts using the authenticated GitHub
// App's default identity; do not impersonate or override the human git author.
import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';

const repo = process.env.GITHUB_REPOSITORY;
if (!process.env.GITHUB_ACTIONS || !repo) throw new Error('Run in GitHub Actions');
function api(endpoint, payload, method) {
  const args = ['api', endpoint];
  if (method) args.push('--method', method);
  if (payload) args.push('--input', '-');
  return JSON.parse(execFileSync('gh', args, {
    input: payload ? JSON.stringify(payload) : undefined,
    encoding: 'utf8',
  }));
}
const tracked = execFileSync('git', ['diff', '--name-only', '--', 'data/phoenix', 'docs/PHOENIX_COVERAGE.md'], { encoding: 'utf8' });
const untracked = execFileSync('git', ['ls-files', '--others', '--exclude-standard', '--', 'data/phoenix', 'docs/PHOENIX_COVERAGE.md'], { encoding: 'utf8' });
const files = [...new Set((tracked + '\n' + untracked).trim().split('\n').filter(Boolean))];
if (files.length) {
  const base = api(`repos/${repo}/git/ref/heads/main`).object.sha;
  const parent = api(`repos/${repo}/git/commits/${base}`);
  const tree = api(`repos/${repo}/git/trees`, {
    base_tree: parent.tree.sha,
    tree: files.map(path => ({ path, mode: '100644', type: 'blob', content: readFileSync(path, 'utf8') })),
  });
  const commit = api(`repos/${repo}/git/commits`, {
    message: `Update Phoenix ${process.env.PHOENIX_COUNTRY || 'global'} public venue facts`,
    tree: tree.sha, parents: [base],
  });
  api(`repos/${repo}/git/refs/heads/main`, { sha: commit.sha, force: false }, 'PATCH');
  console.log(`Saved ${files.length} generated files at ${commit.sha}`);
}
