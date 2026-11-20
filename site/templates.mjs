import { business, services, tours, areas, routes, steps, faqs } from './content.mjs';

export const escape = (value) => String(value).replace(/[&<>"']/g, (character) => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character]);

export const link = (href, label, className = '') =>
  `<a${className ? ` class="${className}"` : ''} href="${escape(href)}">${escape(label)}</a>`;

export const servicePath = (slug) => `/${slug}/`;
export const tourPath = (slug) => `/tours/${slug}/`;
export const areaPath = (slug) => `/taxi-${slug}/`;

const serviceOptions = ['Airport Transfer', 'Local Taxi', 'Tour', 'Golf Tour', 'Corporate Travel', 'Hospital Run', 'Aircoach Run', 'Other'];
const book = '/book/';
const call = `tel:${business.intl}`;
const { whatsapp } = business;

function navGroup(label, items) {
  return `<li><details class="nav-group"><summary>${label}</summary><ul>${items.map(([href, text]) => `<li>${link(href, text)}</li>`).join('')}</ul></details></li>`;
}

export function header() {
  return `<a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header"><div class="shell header-inner">
      <a href="/" class="brand"><img src="/assets/logo/umair-dark.svg" width="205" height="42" alt="Umair Taxi and Limo home"></a>
      <button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" hidden>Menu</button>
      <nav id="site-nav" aria-label="Main navigation"><ul class="nav-list">
        <li>${link('/', 'Home')}</li>
        ${navGroup('Services', [['/services/', 'All Services'], ...services.map(([slug, title]) => [servicePath(slug), title])])}
        ${navGroup('Tours', [['/tours/', 'All Tours'], ...tours.map(([slug, title]) => [tourPath(slug), title]), ['/golf-tours/', 'Golf Tours']])}
        ${navGroup('Service Areas', [['/service-areas/', 'All Service Areas'], ...areas.map(([slug, title]) => [areaPath(slug), title])])}
        <li>${link('/fleet/', 'Fleet')}</li><li>${link('/about/', 'About')}</li><li>${link('/contact/', 'Contact')}</li>
      </ul></nav>
      ${link(book, 'Book Now', 'button button--gold header-book')}
    </div></header>`;
}

export function actions(booking = book) {
  return `<div class="actions">${link(booking, 'Book Now', 'button button--gold')}${link(whatsapp, 'WhatsApp', 'button button--outline')}${link(call, 'Call', 'button button--outline')}</div>`;
}

export function footer() {
  return `<section class="pre-footer"><div class="shell pre-footer-inner">
      <div><h2>Ready to book your journey?</h2><p>Tell us where you need to go and we’ll help arrange the trip.</p></div>
      ${actions()}
    </div></section>
    <footer class="site-footer"><div class="shell">
      <div class="footer-grid">
        <div><a href="/"><img src="/assets/logo/umair-dark.svg" width="205" height="42" alt="Umair Taxi and Limo home"></a><p>Airport transfers, local taxis and private tours from Youghal, Ireland.</p></div>
        <div><h2>Explore</h2>${link('/airport-transfers/', 'Airport Transfers')}${link('/local-taxi-youghal/', 'Local Taxi')}${link('/tours/', 'Ireland Tours')}${link('/service-areas/', 'Service Areas')}</div>
        <div><h2>Plan your journey</h2>${link('/fleet/', 'Fleet')}${link('/how-it-works/', 'How It Works')}${link('/rates/', 'Get a Quote')}${link('/faq/', 'FAQs')}</div>
        <div><h2>Contact</h2><address>${escape(business.address)}<br>${link(call, business.phone)}${link(`mailto:${business.email}`, business.email)}</address></div>
      </div>
      <div class="footer-bottom"><span>© Umair Taxi and Limo</span><div>${link('/privacy-policy/', 'Privacy Policy')}${link('/terms/', 'Terms')}</div></div>
    </div></footer>`;
}

export function bookingForm(compact = false) {
  return `<section class="booking-panel" id="booking" aria-labelledby="booking-title">
    <h2 id="booking-title">${compact ? 'Plan your journey' : 'Journey details'}</h2>
    <p>${compact ? 'Start with your route and travel date.' : 'Prepare an enquiry to send to us on WhatsApp.'}</p>
    <form action="/book/" method="get" ${compact ? 'data-quick-booking' : 'data-full-booking'}>
      <div class="form-grid">
        <label class="full">Trip type<select name="trip">${serviceOptions.map((option) => `<option>${option}</option>`).join('')}</select></label>
        <label>Pickup<input name="pickup" placeholder="Address or town" required maxlength="160"></label>
        <label>Destination<input name="destination" placeholder="Address or airport" required maxlength="160"></label>
        <label>Date<input type="date" name="date" required></label>
        <label>Time <span>(Irish time)</span><input type="time" name="time" required></label>
        ${compact ? '' : `
          <label>Passengers<input type="number" min="1" max="99" name="passengers" value="1" inputmode="numeric" required></label>
          <label>Luggage <span>(optional)</span><input name="luggage" placeholder="Bags or large items" maxlength="140"></label>
          <label data-flight>Flight number <span>(optional)</span><input name="flight" maxlength="20" placeholder="e.g. EI 123"></label>
          <label>Return trip<select name="return"><option>No</option><option>Yes</option></select></label>
          <label class="full">Name<input name="name" autocomplete="name" required maxlength="100"></label>
          <label>Phone<input type="tel" name="phone" autocomplete="tel" required maxlength="35"></label>
          <label>Email <span>(optional)</span><input type="email" name="email" autocomplete="email" maxlength="140"></label>
          <label class="full">Notes <span>(optional)</span><textarea name="notes" rows="3" maxlength="400" placeholder="Return timing, meeting point or special requests"></textarea></label>`}
      </div>
      <button class="button button--gold form-submit" ${compact ? '' : 'hidden'}>${compact ? 'Continue to Booking' : 'Continue to WhatsApp'}</button>
      ${compact ? '' : `<p class="form-note">Your journey is confirmed after we agree the details with you.</p>
      <noscript><p>Send your journey details directly via ${link(whatsapp, 'WhatsApp')} or ${link(call, 'call us')}.</p></noscript>`}
    </form>
  </section>`;
}

export function image(name, alt, eager = false) {
  const width = name === 'cork-coast-drive' ? 1500 : 760;
  const height = name === 'cork-coast-drive' ? 1000 : 500;
  return `<img src="/assets/photos/${name}.webp" alt="${escape(alt)}" width="${width}" height="${height}" ${eager ? 'fetchpriority="high" srcset="/assets/photos/cork-coast-drive-small.webp 760w, /assets/photos/cork-coast-drive.webp 1500w" sizes="(max-width: 760px) 100vw, 75vw"' : 'loading="lazy" decoding="async"'}>`;
}

export function tiles(items) {
  return `<div class="tiles">${items.map(([href, title, description, icon, anchor]) => `<article class="tile"${anchor ? ` id="${anchor}"` : ''} data-reveal>
    ${icon ? `<span class="tile-icon" aria-hidden="true">${icon}</span>` : ''}
    <h3>${link(href, title)}</h3><p>${escape(description)}</p>
  </article>`).join('')}</div>`;
}

export const serviceTiles = () => tiles(services.map(([slug, title, icon, description]) => [servicePath(slug), title, description, icon]));
export const areaTiles = () => tiles(areas.map(([slug, title, description]) => [areaPath(slug), title, description, null, slug === 'county-cork' ? 'co-cork' : slug]));
export const process = () => `<ol class="steps">${steps.map(([title, description]) => `<li data-reveal><h3>${title}</h3><p>${description}</p></li>`).join('')}</ol>`;
export const questions = () => `<div class="questions">${faqs.map(([title, answer]) => `<details><summary>${title}</summary><p>${answer}</p></details>`).join('')}</div>`;
export const section = (title, body, className = '', id = '') => `<section class="section ${className}"${id ? ` id="${id}"` : ''}><div class="shell"><h2>${title}</h2>${body}</div></section>`;

export const tourMedia = {
  ireland: ['irish-atlantic-coast', 'Green headlands overlooking the Irish Atlantic coast'],
  cork: ['cork-harbour-town', 'Pastel buildings and boats in an Irish harbour town'],
  waterford: ['waterford-coastal-cliffs', 'Grassy headlands and slate cliffs on an Irish coast'],
  youghal: ['east-cork-harbour', 'Stone quayside and fishing boats in a coastal town'],
  dungarvan: ['dungarvan-bay-path', 'Walking trail along a tidal bay with hills in the distance'],
  'west-cork': ['cork-harbour-town', 'Pastel buildings and boats in an Irish harbour town'],
  scenic: ['irish-atlantic-coast', 'Green headlands overlooking the Irish Atlantic coast'],
  custom: ['dungarvan-bay-path', 'Walking trail along a tidal bay with hills in the distance'],
};

export function tourTiles(selection = tours) {
  return `<div class="tiles fleet-tiles">${selection.map(([slug, title, description]) => `<article class="tile" id="${slug}" data-reveal>
    ${image(...tourMedia[slug])}<div class="tile-copy"><h3>${link(tourPath(slug), title)}</h3><p>${escape(description)}</p></div>
  </article>`).join('')}</div>`;
}

const vehicles = [
  ['saloon-taxi', 'Saloon taxi', 'A vehicle category to ask about for local trips and airport transfers with standard luggage.'],
  ['people-carrier', 'MPV / people carrier', 'Discuss a people carrier for family airport trips and private tours with extra bags.'],
  ['group-vehicle', 'Large group vehicle', 'Enquire about transport for a group tour, corporate event or airport trip with several passengers.'],
];
export function fleet() {
  return `<div class="tiles fleet-tiles">${vehicles.map(([name, title, description]) => `<article class="tile" data-reveal>
    ${image(name, `Illustrative example of a ${title.toLowerCase()}`)}<div class="tile-copy"><h3>${title}</h3><p>${description}</p></div>
  </article>`).join('')}</div><p class="section-note">Images illustrate vehicle categories. Share your passenger and luggage requirements to discuss availability.</p>`;
}

export function home() {
  return `<section class="hero">
    <div class="hero-media">${image('cork-coast-drive', '', true)}</div>
    <div class="shell hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Based in Youghal, Ireland</p>
        <h1>Airport transfers<br> &amp; local taxi<br> <em>from Youghal.</em></h1>
        <p class="hero-intro">From a Cork Airport pickup to a day exploring Ireland, arrange a journey around your plans.</p>
        ${actions('#booking')}
      </div>
      ${bookingForm(true)}
    </div>
  </section>
  <div class="route-strip" id="areas"><div class="shell">${link('/service-areas/', 'Service Areas', 'area-label')}${areas.slice(0, 4).map(([slug, title]) => link(areaPath(slug), title)).join('')}</div></div>
  <section class="section"><div class="shell">
    <h2>Find the right ride</h2>
    ${tiles([
      ['/airport-transfers/', 'Airport Transfers', services[0][3], '✈️'],
      ['/local-taxi-youghal/', 'Local Taxi', services[1][3], '🚕'],
      ['/tours/', 'Ireland Tours', 'Plan a private trip through Cork, Waterford or further across Ireland.', '🗺️'],
    ])}
    <p class="section-note">${link('/services/', 'View all services', 'text-link')}</p>
  </div></section>
  <section class="tour-feature" id="tours"><div class="shell feature-grid">
    <figure data-reveal>${image('irish-atlantic-coast', 'Green headlands overlooking the Atlantic on the Irish coast')}</figure>
    <div data-reveal><h2>Explore Ireland with us.</h2><p>Make time for harbour towns, coastal roads and the places you’ve always wanted to see. Start with a region or tell us the route you have in mind.</p>
      <div class="actions">${link('/tours/', 'View Tours', 'button button--gold')}${link(tourPath('custom'), 'Custom Tour', 'button button--outline')}</div>
    </div>
  </div></section>
  ${section('Ideas for a day out', tourTiles(tours.filter(([slug]) => ['cork', 'waterford', 'youghal'].includes(slug))))}
  ${section('Popular routes', `<div class="route-list">${routes.map(([pickup, destination]) => {
    const query = new URLSearchParams({ pickup, destination, trip: destination.includes('Airport') ? 'Airport Transfer' : 'Local Taxi' });
    return link(`/book/?${query}`, `${pickup} → ${destination}`);
  }).join('')}</div>`)}
  ${section('How it works', process(), 'surface')}
  ${section('Vehicle options', fleet() + `<p class="section-note">${link('/fleet/', 'View Fleet', 'button button--dark')}</p>`, '', 'fleet')}
  ${section('Frequently asked questions', questions(), 'surface', 'faq')}`;
}

export function prose(blocks) {
  return `<div class="copy-blocks">${blocks.map(([title, description]) => `<section><h2>${escape(title)}</h2><p>${escape(description)}</p></section>`).join('')}</div>`;
}
