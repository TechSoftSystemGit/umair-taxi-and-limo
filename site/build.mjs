import { cp, mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { business, services, tours, areas, faqs } from './content.mjs';
import { areaExperience, areaMedia, areaPlanning, serviceExperience, serviceHeroMedia, serviceMedia, servicePlanning } from './detail-content.mjs';
import { regionalTours, stopsByTour, tourFeatureMedia, tourMedia } from './tour-content.mjs';
import { fleetHero, fleetPath, vehicles } from './fleet-content.mjs';
import { icon } from './icons.mjs';
import {
  areaPath, areaTiles, bookingForm, contactForm, escape, fleet, fleetDetails, fleetShowcase, footer, header, home, image,
  journeyFeature, journeySteps, link, process, prose, questions, section, servicePath, serviceTiles, tiles, tourPath, tourTiles,
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
const serviceGuide = journeySteps('From enquiry to pickup', 'Include your route, preferred date, passenger count and luggage.');
page('/services/', 'Taxi & Transfer Services', 'Explore airport transfers, local taxis, golf transport, corporate trips, hospital runs and Aircoach connections from Youghal.',
  section('Book a journey', serviceTiles()) +
  journeyFeature(serviceHeroMedia['airport-transfers'], 'One place to arrange your travel',
    'From our base in Youghal, enquire about Cork Airport transfers, local taxi trips or a private Ireland tour. Share the plans you want to make and we’ll discuss the journey with you.',
    ['/book/', 'Plan a Journey', 'button button--gold', 'calendar']) + serviceGuide);
for (const [slug, title, icon, description, blocks] of services) {
  const trip = {
    'airport-transfers': 'Airport Transfer', 'local-taxi-youghal': 'Local Taxi',
    'golf-tours': 'Golf Tour', 'corporate-travel': 'Corporate Travel',
    'hospital-runs': 'Hospital Run', 'aircoach-transfers': 'Aircoach Run',
  }[slug];
  const booking = '/book/?' + new URLSearchParams({ trip });
  const [featureTitle, featureCopy, enquiryDetails] = serviceExperience[slug];
  page(servicePath(slug), slug === 'airport-transfers' ? 'Cork Airport Transfers' : title, description,
    `<div class="shell reading service-layout">${prose([...blocks, servicePlanning[slug]])}
      <aside class="quote-band"><div><h2>Request a quote</h2><p>Send your route, travel date and passenger count so we can discuss availability and price.</p></div>
      <div class="actions">${link(booking, 'Get Quote', 'button button--gold', 'calendar')}${link('/service-areas/', 'Service Areas', 'button button--dark', 'pin')}</div></aside></div>
      ${journeyFeature(serviceMedia[slug], featureTitle, featureCopy, [booking, 'Plan Your Journey', 'button button--gold', 'calendar'])}
      ${journeySteps('How to arrange your pickup', enquiryDetails + '.')}
      ${section('Explore other services', serviceTiles(services.filter(([otherSlug]) => otherSlug !== slug)), 'surface')}`,
    { parent: ['/services/', 'Services'], schema: 'Service', media: serviceHeroMedia[slug], icon, booking, introStyle: 'service-intro' });
}
const allTours = [...tours, ...regionalTours];
const tourBooking = '/book/?trip=Tour';
const tourJump = `<nav class="shell tour-jump" aria-label="Tour categories">${link('#local-tours', 'South Coast')}${link('#nationwide', 'All Around Ireland')}${link(tourPath('custom'), 'Custom Tours')}</nav>`;
const regionalOptions = section('Explore Ireland by region',
  '<p class="section-lead">Browse example itineraries for the west coast, the north and inland Ireland. Choose a destination to see suggested stops and plan your enquiry.</p>' + tourTiles(regionalTours),
  'surface tour-catalogue', 'nationwide');
page('/tours/', 'Tours around Ireland', 'Explore private tour ideas from Youghal and across Ireland, from the south coast to Kerry, Galway, Donegal and the Causeway Coast.',
  tourJump + section('Tours from the south coast', tourTiles(tours.filter(([slug]) => !['ireland', 'scenic', 'custom'].includes(slug))), 'tour-catalogue', 'local-tours')
  + regionalOptions + section('Plan your own itinerary', tourTiles(tours.filter(([slug]) => ['ireland', 'scenic', 'custom'].includes(slug))), 'tour-catalogue', 'custom-tours')
  + journeyFeature(['tour-island-road', 'Illustrative Irish country road leading towards the sea'], 'See the places you came for',
    'Tell us where you’d like to start, which stops matter most and how much time you have. We’ll discuss the route and availability with you.',
    [tourBooking, 'Plan a Tour', 'button button--gold', 'calendar']),
  { media: tourMedia.ireland, introStyle: 'tour-hub-intro', booking: tourBooking, introLabel: 'Plan a Tour', introSecondary: ['#nationwide', 'Browse Destinations'] });

for (const [index, [slug, title, description, detail]] of allTours.entries()) {
  const booking = '/book/?' + new URLSearchParams({ trip: 'Tour', destination: title });
  const include = stopsByTour[slug].map((stop) => `<li>${icon('pin')}${escape(stop)}</li>`).join('');
  const collection = index < tours.length ? tours : regionalTours;
  const current = index < tours.length ? index : index - tours.length;
  const otherTours = [collection[(current + 1) % collection.length], collection[(current + 2) % collection.length]];
  page(tourPath(slug), title, description,
    `<section class="shell tour-itinerary${index % 2 ? ' tour-itinerary--reverse' : ''}">
      <div><h2>Ideas for your route</h2><p>${escape(detail)}</p></div>
      <div class="tour-stops"><h3>Stops to consider</h3><ul>${include}</ul></div>
    </section>
    ${journeyFeature(tourFeatureMedia[slug], 'A tour shaped around your group',
      'Tell us where you’re staying, how much time you have and the stops you want to prioritise. We’ll discuss a route, pickup options and availability for your group.',
      [booking, 'Enquire About This Tour', 'button button--gold', 'calendar'])}
    ${journeySteps('How to plan your tour', 'Share your dates, pickup location, group size and must-see stops.')}
    ${section('Explore more tours', tourTiles(otherTours) + `<p class="section-note">${link('/tours/#nationwide', 'Browse All Destinations', 'button button--dark', 'map')}</p>`, 'surface tour-catalogue')}`,
    { parent: ['/tours/', 'Tours around Ireland'], schema: 'Service', media: tourMedia[slug], booking, introStyle: 'service-intro tour-intro', introLabel: 'Enquire About This Tour' });
}

page('/service-areas/', 'Taxi and Transfer Service Areas', 'Explore pickups from our base in Youghal and across Cork, Waterford, Dungarvan, County Cork and West Waterford.',
  section('Where we serve', areaTiles()) +
  journeyFeature(areaMedia.youghal, 'Based on the East Cork coast',
    'Start in Youghal or ask about pickups in Cork, Waterford and Dungarvan. If you’re meeting outside a town, an Eircode or map pin will help us discuss the exact pickup point.',
    [areaPath('youghal'), 'Explore Youghal Pickups', 'button button--gold', 'pin']) +
  journeySteps('Arranging a pickup', 'Share your address or meeting point, destination, date and passenger count.'),
  { crumb: 'Service Areas' });
for (const [slug, place, description, detail, route, tour] of areas) {
  const [pickup, destination] = route.split(' → ');
  const query = new URLSearchParams({ pickup, destination, trip: destination.includes('Airport') ? 'Airport Transfer' : 'Local Taxi' });
  const booking = '/book/?' + new URLSearchParams({ pickup: place });
  page(areaPath(slug), `Taxi and Airport Transfers in ${place}`, description,
    `<div class="shell reading detail-layout">${prose([[ `Pickups in ${place}`, detail ], areaPlanning[slug]])}
    <aside class="detail-aside"><h2>Example journey</h2><p>${link('/book/?' + query, route, 'text-link', 'pin')}</p>
      <div class="actions">${link(booking, 'Book Now', 'button button--gold', 'calendar')}${link(whatsapp, 'WhatsApp', 'button button--dark', 'chat')}</div></aside></div>
    ${journeyFeature(tourMedia[tour], `Plan your pickup in ${place}`, areaExperience[slug], [booking, 'Enquire About a Pickup', 'button button--gold', 'pin'])}
    ${journeySteps('From pickup to destination', `Include your meeting point in ${place}, the date and where you’re heading.`)}
    ${section(`Travel options in ${place}`, serviceTiles(services.slice(0, 2)) + `<p class="section-note">${link(tourPath(tour), 'Explore Local Tours', 'button button--dark', 'map')}</p>`, 'surface')}`,
    { parent: ['/service-areas/', 'Service Areas'], schema: 'Service', media: areaMedia[slug], icon: 'pin', booking });
}

page('/fleet/', 'Our Fleet', 'Compare vehicle options for a Cork Airport transfer, local taxi ride or private tour, from a saloon to a larger group vehicle.',
  fleetShowcase() + journeyFeature(
    ['about-journey-detail', 'Illustrative passenger pickup with luggage beside the vehicle'],
    'Find the right fit for your trip',
    'Tell us how many people are travelling and what you’ll bring. We’ll check which vehicle can accommodate your group and luggage before confirming the booking.',
    ['/book/', 'Request a Quote', 'button button--gold', 'calendar']),
  { crumb: 'Fleet', media: ['cork-coast-drive-small', 'Illustrative taxi on a coastal road in County Cork'], introStyle: 'service-intro fleet-overview-intro',
    introLabel: 'Request a Quote', introSecondary: ['#vehicles', 'Explore Vehicles'] });
for (const vehicle of vehicles) {
  const booking = '/book/?' + new URLSearchParams({ notes: 'Vehicle preference: ' + vehicle.title });
  page(fleetPath(vehicle.slug), vehicle.title, vehicle.description,
    fleetDetails(vehicle, booking) + section('Compare other vehicles', fleet(vehicles.filter((option) => option !== vehicle)), 'surface'),
    { parent: ['/fleet/', 'Fleet'], media: fleetHero(vehicle), icon: vehicle.icon, booking, introLabel: 'Enquire About This Vehicle',
      introStyle: 'service-intro fleet-detail-hero', introSecondary: ['#vehicle-gallery', 'View Vehicle Gallery'] });
}
page('/about/', 'About Umair Taxi and Limo', 'Meet Umair Taxi and Limo, a Youghal-based taxi, airport transfer and private tour business serving Cork and Waterford.', `
  <section class="shell reading about-story">
    <div><p class="eyebrow">Based in Youghal</p><h2>From the East Cork coast</h2>
      <p>Youghal is our starting point. We arrange local taxi trips around town, pickups and drop-offs at Cork Airport, and private tours across Ireland.</p>
      <p>For journeys starting in Cork, Waterford or Dungarvan, share your pickup point and the time you need to arrive. For tours, tell us which stops you’d like to include.</p>
      <div class="actions">${link('/service-areas/', 'Service Areas', 'button button--dark', 'pin')}${link('/contact/', 'Contact Us', 'button button--gold', 'mail')}</div>
    </div>
    <figure>${image('about-journey-detail', 'Illustrative close-up of a passenger door being opened beside luggage')}</figure>
  </section>
  ${section('How we can help you travel', tiles([
    ['/airport-transfers/', 'Cork Airport Transfers', services[0][3], 'plane'],
    ['/local-taxi-youghal/', 'Local Taxi', services[1][3], 'taxi'],
    ['/tours/', 'Private Ireland Tours', 'Discuss a private itinerary from the East Cork coast or across Ireland.', 'map'],
  ]), 'surface')}`, { schema: 'AboutPage', crumb: 'About', media: ['about-youghal-harbour', 'Illustrative view of the Youghal waterfront and harbour at dawn'], introStyle: 'about-intro' });
page('/contact/', 'Contact Umair Taxi and Limo', 'Contact our Youghal taxi and transfer business by phone, WhatsApp or email to discuss your journey.', `<div class="shell reading contact-layout">
  <section class="contact detail-aside"><h2>Get in touch</h2>
  <address><p>${icon('pin')}${escape(address)}</p><p>${link('tel:' + intl, phone, '', 'phone')}<br>${link('mailto:' + email, email, '', 'mail')}<br>${link(whatsapp, 'WhatsApp', '', 'chat')}</p></address>
  ${link('/book/', 'Book Now', 'button button--dark', 'calendar')}</section>
  ${contactForm()}</div>`, { schema: 'ContactPage', crumb: 'Contact', icon: 'mail' });
page('/book/', 'Book a Taxi or Transfer', 'Request a quote for an airport transfer, local taxi or private Ireland tour with pickup and travel details.', `<div class="shell reading book-layout">${bookingForm()}</div>`, { crumb: 'Book' });
page('/how-it-works/', 'How Booking Works', 'See how to request a journey, share pickup details and confirm a booking with Umair Taxi and Limo.', section('From enquiry to pickup', process()));
page('/rates/', 'Request a Taxi Quote', 'Request a quote for your taxi, airport transfer or tour based on your route and group details.', `<div class="shell reading">${prose([
  ['What to include', 'Send your pickup, destination, preferred date and time, passenger count and luggage. Include a return trip or additional stops if you need them.'],
])}${related([['/book/', 'Get Quote'], [whatsapp, 'WhatsApp']])}</div>`);
page('/faq/', 'Taxi, Transfer and Tour FAQs', 'Find answers about arranging local taxis, airport pickups, quotes and private Ireland tours from Youghal.', section('Booking questions', questions()), { schema: 'FAQPage', crumb: 'FAQs' });
page('/privacy-policy/', 'Privacy Policy', 'How the booking form prepares your enquiry and how to contact Umair Taxi and Limo about your information.', `<div class="shell reading">${prose([
  ['Information in an enquiry', 'The booking and contact forms prepare a message in your browser. If you send it through WhatsApp or your email app, we receive the details you choose to share so we can respond to your enquiry. Your chosen messaging service also processes the message.'],
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
  <link rel="icon" type="image/svg+xml" href="/assets/logo/umair-icon.svg?v=3">
  <link rel="preload" href="/assets/fonts/instrument-serif.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css?v=11">
  <script src="/assets/site.js?v=3" defer></script>
  <script type="application/ld+json">${schema(path, data, data.home ? [['/', 'Home']] : crumbs)}</script>
</head>
<body>
  ${header()}
  <main id="main">${data.home ? '' : `<div class="page-intro${data.introStyle ? ' ' + data.introStyle : ''}"><div class="shell intro-grid">
    <div class="page-intro-copy"><nav class="crumbs" aria-label="Breadcrumb"><ol>${crumbs.map(([href, label], index) => `<li>${index === crumbs.length - 1 ? `<span aria-current="page">${escape(label)}</span>` : link(href, label)}</li>`).join('')}</ol></nav>
    <h1>${icon(data.icon)}${escape(data.title)}</h1><p>${escape(data.description)}</p>
    ${path === '/book/' || path === '/contact/' ? '' : link(data.booking || '/book/', data.introLabel || 'Book Now', 'button button--gold', 'calendar')}
    ${data.introSecondary ? link(...data.introSecondary, 'button button--outline intro-secondary', 'map') : ''}</div>
    ${data.media ? `<figure>${image(...data.media, true)}</figure>` : ''}
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
  const html = render(path, data).replace(/[ \t]+$/gm, '');
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

export const generatedPages = [...pages.keys()].map((path) => path.slice(1) + 'index.html');
