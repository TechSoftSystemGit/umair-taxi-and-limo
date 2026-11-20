import { createServer } from 'node:http';
import { createReadStream } from 'node:fs';
import { readFile, stat } from 'node:fs/promises';
import { extname, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('./dist/', import.meta.url));
const redirects = JSON.parse(await readFile(new URL('./dist/redirects.json', import.meta.url), 'utf8'));
const types = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
  '.woff2': 'font/woff2',
  '.txt': 'text/plain; charset=utf-8',
  '.xml': 'application/xml; charset=utf-8',
};

const server = createServer(async (request, response) => {
  function end(status, message, headers) {
    response.writeHead(status, { 'Content-Type': 'text/plain; charset=utf-8', ...headers });
    response.end(request.method === 'HEAD' ? undefined : message);
  }
  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return end(405, 'Method not allowed', { Allow: 'GET, HEAD' });
  }
  let url;
  let path;
  try {
    url = new URL(request.url, 'http://localhost');
    path = decodeURIComponent(url.pathname);
  } catch {
    return end(400, 'Invalid URL');
  }
  if (path.includes('\\') || path.includes('\0') || path.split('/').some((segment) => segment.startsWith('.'))) {
    return end(404, 'Page not found');
  }

  const redirect = Object.hasOwn(redirects, path) ? redirects[path] : undefined;
  if (redirect) return end(301, 'Moved permanently', { Location: redirect + url.search });

  const normalized = path.endsWith('/') ? path + 'index.html' : path;
  const type = types[extname(normalized)];
  if (!type) {
    const directoryIndex = resolve(root, '.' + path, 'index.html');
    if (path.startsWith('/') && !path.startsWith('//') && directoryIndex.startsWith(resolve(root) + sep)) {
      try {
        if ((await stat(directoryIndex)).isFile()) {
          return end(301, 'Moved permanently', { Location: url.pathname + '/' + url.search });
        }
      } catch (error) {
        if (error.code !== 'ENOENT' && error.code !== 'ENOTDIR') return end(500, 'Server error');
      }
    }
    return end(404, 'Page not found');
  }

  const file = resolve(root, '.' + normalized);
  if (!file.startsWith(resolve(root) + sep)) return end(404, 'Page not found');
  try {
    const metadata = await stat(file);
    if (!metadata.isFile()) return end(404, 'Page not found');
    response.writeHead(200, {
      'Content-Type': type,
      'Content-Length': metadata.size,
      'Cache-Control': path.startsWith('/assets/') ? 'public, max-age=86400' : 'no-cache',
      'X-Content-Type-Options': 'nosniff',
      'Referrer-Policy': 'strict-origin',
    });
    if (request.method === 'HEAD') return response.end();
    const stream = createReadStream(file);
    stream.on('error', () => response.destroy());
    stream.pipe(response);
  } catch (error) {
    if (error.code === 'ENOENT' || error.code === 'ENOTDIR') return end(404, 'Page not found');
    end(500, 'Server error');
  }
});

const port = Number(process.env.PORT || 3000);
server.listen(port, process.env.HOST || '0.0.0.0', () => {
  console.log(`Umair Taxi and Limo listening on port ${server.address().port}`);
});
