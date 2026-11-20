import { cp, mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { business, services, tours, areas, faqs } from './content.mjs';
import {
  areaPath, areaTiles, bookingForm, escape, fleet, footer, header, home, image,
  link, process, prose, questions, section, servicePath, serviceTiles, tourMedia, tourPath, tourTiles,
} from './templates.mjs';

const output = 'dist';
const { origin, name, phone, intl, email, whatsapp, address } = business;
const orgId = origin + '/#business';

const pages = new Map();
function page(path, title, description, content, options = {}) {
  pages.set(path, { title, description, content, ...options });
}
function related(items) {
  return `<aside class="related"><h2>Plan your journey</h2><div class="actions">${items.map(([href, text]) => link(href, text, 'button button--dark')).join('')}</div></aside>`;
}

page('/', 'Cork Airport Transfers & Taxi from Youghal', 'Arrange a Cork Airport transfer, local taxi or private Ireland tour with Umair Taxi and Limo in Youghal, County Cork.', home(), { home: true });
page('/services/', 'Taxi & Transfer Services', 'Explore airport transfers, local taxis, golf transport, corporate trips, hospital runs and Aircoach connections from Youghal.', section('Book a journey', serviceTiles()));
for (const [slug, title, , description, blocks] of services) {
  const trip = {
    'airport-transfers': 'Airport Transfer', 'local-taxi-youghal': 'Local Taxi',
    'golf-tours': 'Golf Tour', 'corporate-travel': 'Corporate Travel',
    'hospital-runs': 'Hospital Run', 'aircoach-transfers': 'Aircoach Run',
  }[slug];
  page(servicePath(slug), slug === 'airport-transfers' ? 'Cork Airport Transfers' : title, description,
    `<div class="shell reading">${prose(blocks)}${related([['/book/?' + new URLSearchParams({ trip }), 'Get Quote'], ['/service-areas/', 'Service Areas']])}</div>`,
    { parent: ['/services/', 'Services'], schema: 'Service', media: ['airport-transfers', 'local-taxi-youghal'].includes(slug)
      ? ['cork-coast-drive-small', 'Illustrative saloon car on an Irish coastal road'] : undefined });
}
page('/tours/', 'Private Ireland Tours', 'Plan a private tour from Youghal through Cork, Waterford, Dungarvan or further across Ireland.', section('Choose a region or plan your own route', tourTiles()), { media: tourMedia.ireland });
for (const [slug, title, description, detail] of tours) {
  page(tourPath(slug), title, description, `<div class="shell reading">${prose([
    ['Ideas for your route', detail],
    ['Pickup and group details', 'Ask about starting in Youghal, Cork, Waterford or Dungarvan. Share your pickup address, group size, luggage and any mobility needs so we can discuss the trip with you.'],
  ])}${related([['/book/?trip=Tour', 'Enquire'], ['/tours/', 'View Tours']])}</div>`, { parent: ['/tours/', 'Tours'], schema: 'Service', media: tourMedia[slug] });
}

page('/service-areas/', 'Taxi and Transfer Service Areas', 'Explore pickups from our base in Youghal and across Cork, Waterford, Dungarvan, County Cork and West Waterford.', section('Where we serve', areaTiles()), { crumb: 'Service Areas' });
for (const [slug, place, description, detail, route, tour] of areas) {
  const [pickup, destination] = route.split(' → ');
  const query = new URLSearchParams({ pickup, destination, trip: destination.includes('Airport') ? 'Airport Transfer' : 'Local Taxi' });
  page(areaPath(slug), `Taxi and Airport Transfers in ${place}`, description,
    `<div class="shell reading">${prose([[ `Pickups in ${place}`, detail ]])}
    <section class="related"><h2>Example journey</h2><p>${link('/book/?' + query, route, 'text-link')}</p></section>
    ${related([['/book/?' + new URLSearchParams({ pickup: place }), 'Book Now'], [whatsapp, 'WhatsApp'], ['/airport-transfers/', 'Airport Transfers'], ['/local-taxi-youghal/', 'Local Taxi'], [tourPath(tour), 'Local Tours']])}</div>`, { parent: ['/service-areas/', 'Service Areas'], schema: 'Service' });
}

page('/fleet/', 'Vehicle Options', 'Discuss saloon, people carrier and group vehicle options when enquiring about a taxi, airport transfer or Irish tour.', section('Find a vehicle for your journey', fleet()), { crumb: 'Fleet' });
page('/about/', 'About Umair Taxi and Limo', 'Meet Umair Taxi and Limo, a Youghal-based taxi, airport transfer and private tour business serving Cork and Waterford.', `<div class="shell reading">${prose([
  ['Based in Youghal', 'We arrange local taxi trips in and around Youghal, journeys to and from Cork Airport, and private tours across Ireland. Ask about pickups from East Cork, Dungarvan and Waterford.'],
  ['Tell us where you need to go', 'Get in touch with your pickup, destination and travel date. For tours, share the places you want to visit and we can discuss a route.'],
])}${related([['/contact/', 'Contact'], ['/airport-transfers/', 'Airport Transfers'], ['/tours/', 'View Tours']])}</div>`, { schema: 'AboutPage', crumb: 'About' });
page('/contact/', 'Contact Umair Taxi and Limo', 'Contact our Youghal taxi and transfer business by phone, WhatsApp or email to discuss your journey.', `<section class="shell reading contact"><h2>Get in touch</h2>
  <address><p>${escape(address)}</p><p>${link('tel:' + intl, phone)}<br>${link('mailto:' + email, email)}<br>${link(whatsapp, 'WhatsApp')}</p></address>
  ${link('/book/', 'Book Now', 'button button--dark')}</section>`, { schema: 'ContactPage', crumb: 'Contact' });
page('/book/', 'Book a Taxi or Transfer', 'Request a quote for an airport transfer, local taxi or private Ireland tour with pickup and travel details.', `<div class="shell reading book-layout">${bookingForm()}</div>`, { crumb: 'Book' });
page('/how-it-works/', 'How Booking Works', 'See how to request a journey, share pickup details and confirm a booking with Umair Taxi and Limo.', section('From enquiry to pickup', process()));
page('/rates/', 'Request a Taxi Quote', 'Request a quote for your taxi, airport transfer or tour based on your route and group details.', `<div class="shell reading">${prose([
  ['What to include', 'Send your pickup, destination, preferred date and time, passenger count and luggage. Include a return trip or additional stops if you need them.'],
])}${related([['/book/', 'Get Quote'], [whatsapp, 'WhatsApp']])}</div>`);
page('/faq/', 'Taxi, Transfer and Tour FAQs', 'Find answers about arranging local taxis, airport pickups, quotes and private Ireland tours from Youghal.', section('Booking questions', questions()), { schema: 'FAQPage', crumb: 'FAQs' });
page('/privacy-policy/', 'Privacy Policy', 'How the booking form prepares your enquiry and how to contact Umair Taxi and Limo about your information.', `<div class="shell reading">${prose([
  ['Information in an enquiry', 'The booking form prepares a message in your browser. If you send it through WhatsApp, we receive the trip details and contact information you choose to share so we can respond to your enquiry. WhatsApp processes messages through its own service.'],
  ['Contact us about your information', `Email ${email} to ask about information you have shared with us or request a correction.`],
])}</div>`);
page('/terms/', 'Booking Terms', 'What to expect when you request and confirm travel with Umair Taxi and Limo.', `<div class="shell reading">${prose([
  ['Enquiries and confirmation', 'Submitting journey details starts an enquiry. Your journey is confirmed once we agree availability, pickup details and the quote with you.'],
  ['Changes to your journey', `If your plans change, contact us on ${phone} to discuss the booking.`],
])}</div>`);

export const redirects = {
  '/index.html': '/', '/services.html': '/services/', '/tours.html': '/tours/',
  '/service-areas.html': '/service-areas/', '/about.html': '/about/', '/contact.html': '/contact/',
  '/faq.html': '/faq/', '/fleet.html': '/fleet/', '/rates.html': '/rates/', '/how-it-works.html': '/how-it-works/',
  '/services/local-taxi.html': '/local-taxi-youghal/', '/services/ireland-tours.html': '/tours/',
  '/services/hotel-golf-transfers.html': '/golf-tours/', '/services/corporate-chauffeur.html': '/corporate-travel/',
  '/services/city-to-city.html': '/service-areas/',
  ...Object.fromEntries(services.map(([slug]) => [`/services/${slug}.html`, servicePath(slug)]).filter(([old]) => old !== '/services/local-taxi-youghal.html')),
};

function schema(path, data, crumbs) {
  const url = origin + path;
  const graph = [{
    '@type': 'LocalBusiness', '@id': orgId, name, url: origin + '/', telephone: intl, email,
    address: { '@type': 'PostalAddress', streetAddress: 'Istanbul Bites, Upper Cork Hill', addressLocality: 'Youghal', addressCountry: 'IE' },
    areaServed: areas.map(([, place]) => place),
  }, {
    '@type': 'WebSite', '@id': origin + '/#website', url: origin + '/', name, publisher: { '@id': orgId },
  }, {
    '@type': ['AboutPage', 'ContactPage', 'FAQPage'].includes(data.schema) ? data.schema : 'WebPage',
    '@id': url + '#page', url, name: data.title, description: data.description, isPartOf: { '@id': origin + '/#website' },
    ...(crumbs.length > 1 ? { breadcrumb: { '@id': url + '#breadcrumb' } } : {}),
    ...(data.schema === 'FAQPage' ? { mainEntity: faqs.map(([question, answer]) => ({
      '@type': 'Question', name: question, acceptedAnswer: { '@type': 'Answer', text: answer },
    })) } : {}),
  }];
  if (crumbs.length > 1) graph.push({
    '@type': 'BreadcrumbList', '@id': url + '#breadcrumb',
    itemListElement: crumbs.map(([href, label], index) => ({
      '@type': 'ListItem', position: index + 1, item: origin + href, name: label,
    })),
  });
  if (data.schema === 'Service') graph.push({
    '@type': 'Service', name: data.title, url, description: data.description, provider: { '@id': orgId },
  });
  return JSON.stringify({ '@context': 'https://schema.org', '@graph': graph }).replaceAll('<', '\\u003c');
}

function render(path, data) {
  const url = origin + path;
  const title = data.title + ' | ' + name;
  const crumbs = [['/', 'Home'], ...(data.parent ? [data.parent] : []), [path, data.crumb || data.title]];
  return `<!doctype html>
<html lang="en-IE">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escape(title)}</title>
  <meta name="description" content="${escape(data.description)}">
  <link rel="canonical" href="${url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_IE">
  <meta property="og:title" content="${escape(title)}">
  <meta property="og:description" content="${escape(data.description)}">
  <meta property="og:url" content="${url}">
  <meta property="og:image" content="${origin}/assets/photos/${data.media?.[0] || 'cork-coast-drive'}.webp">
  <link rel="icon" type="image/svg+xml" href="/assets/logo/umair-icon.svg">
  <link rel="preload" href="/assets/fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css">
  <script src="/assets/site.js" defer></script>
  <script type="application/ld+json">${schema(path, data, data.home ? [['/', 'Home']] : crumbs)}</script>
</head>
<body>
  ${header()}
  <main id="main">${data.home ? '' : `<div class="page-intro"><div class="shell intro-grid">
    <div><nav class="crumbs" aria-label="Breadcrumb"><ol>${crumbs.map(([href, label], index) => `<li>${index === crumbs.length - 1 ? `<span aria-current="page">${escape(label)}</span>` : link(href, label)}</li>`).join('')}</ol></nav>
    <h1>${escape(data.title)}</h1><p>${escape(data.description)}</p>
    ${path === '/book/' ? '' : link('/book/', 'Book Now', 'button button--gold')}</div>
    ${data.media ? `<figure>${image(...data.media)}</figure>` : ''}
  </div></div>`}
  ${data.content}
  </main>
  ${footer()}
</body>
</html>
`;
}

async function emit(path, contents) {
  const directory = join(output, path);
  await mkdir(directory, { recursive: true });
  await writeFile(join(directory, 'index.html'), contents);
}

await mkdir(output, { recursive: true });
await cp('site/assets', join(output, 'assets'), { recursive: true });
const titles = new Set();
const descriptions = new Set();
const documents = new Map();
for (const [path, data] of pages) {
  if (titles.has(data.title) || descriptions.has(data.description)) throw new Error(`Duplicate metadata at ${path}`);
  titles.add(data.title);
  descriptions.add(data.description);
  const html = render(path, data);
  if ((html.match(/<h1>/g) || []).length !== 1) throw new Error(`Invalid H1 at ${path}`);
  documents.set(path, html);
}
for (const [path, html] of documents) {
  for (const [, href] of html.matchAll(/(?:href|src)="(\/[^"#?]*)/g)) {
    if (href.startsWith('/assets/')) await readFile(join(output, href));
    else if (!pages.has(href)) throw new Error(`Broken link ${href} from ${path}`);
  }
  await emit(path, html);
}
for (const target of Object.values(redirects)) {
  if (!pages.has(target)) throw new Error(`Unknown redirect target ${target}`);
}
await writeFile(join(output, 'redirects.json'), JSON.stringify(redirects, null, 2));
await writeFile(join(output, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${origin}/sitemap.xml\n`);
await writeFile(join(output, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${[...pages.keys()].map((path) => `  <url><loc>${origin}${path}</loc></url>`).join('\n')}\n</urlset>\n`);
console.log(`Built ${pages.size} pages and ${Object.keys(redirects).length} legacy redirects.`);
