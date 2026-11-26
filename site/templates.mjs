import { business, services, tours, areas, routes, steps, faqs } from './content.mjs';
import { areaMedia, serviceMedia } from './detail-content.mjs';
import { icon as renderIcon } from './icons.mjs';
import { tourMedia } from './tour-content.mjs';
import { departures, departurePath } from './day-tours.mjs';
import { fleetPath, fleetPhotos, vehicles } from './fleet-content.mjs';

export const escape = (value) => String(value).replace(/[&<>"']/g, (character) => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character]);

export const link = (href, label, className = '', icon = '') =>
  `<a${className ? ` class="${className}"` : ''} href="${escape(href)}">${renderIcon(icon)}${escape(label)}</a>`;

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
      <a href="/" class="brand"><img src="/assets/logo/umair-dark.svg?v=4" width="158" height="50" alt="Umair Taxi and Limo home"></a>
      <button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" hidden>Menu</button>
      <nav id="site-nav" aria-label="Main navigation"><ul class="nav-list">
        <li>${link('/', 'Home')}</li>
        ${navGroup('Services', [['/services/', 'All Services'], ...services.map(([slug, title]) => [servicePath(slug), title])])}
        ${navGroup('Tours', [['/tours/', 'All Day Tours'], ...departures.map(([slug, place]) => [departurePath(slug), 'From ' + place])])}
        ${navGroup('Service Areas', [['/service-areas/', 'All Service Areas'], ...areas.map(([slug, title]) => [areaPath(slug), title])])}
        <li>${link('/fleet/', 'Fleet')}</li><li>${link('/about/', 'About')}</li><li>${link('/contact/', 'Contact')}</li>
      </ul></nav>
      ${link(book, 'Book Now', 'button button--gold header-book')}
    </div></header>`;
}

export function actions(booking = book) {
  return `<div class="actions">${link(booking, 'Book Now', 'button button--gold', 'calendar')}${link(whatsapp, 'WhatsApp', 'button button--outline', 'chat')}${link(call, 'Call', 'button button--outline', 'phone')}</div>`;
}

export function footer() {
  return `<section class="pre-footer"><div class="shell pre-footer-inner">
      <div><h2>Ready to book your journey?</h2><p>Tell us where you need to go and we’ll help arrange the trip.</p></div>
      ${actions()}
    </div></section>
    <footer class="site-footer"><div class="shell">
      <div class="footer-grid">
        <div><a href="/"><img src="/assets/logo/umair-dark.svg?v=4" width="158" height="50" alt="Umair Taxi and Limo home"></a><p>Airport transfers, local taxis and private tours from Youghal, Ireland.</p></div>
        <div><h2>Explore</h2>${link('/airport-transfers/', 'Airport Transfers')}${link('/local-taxi-youghal/', 'Local Taxi')}${link('/tours/', 'Ireland Tours')}${link('/service-areas/', 'Service Areas')}</div>
        <div><h2>Plan your journey</h2>${link('/fleet/', 'Fleet')}${link('/how-it-works/', 'How It Works')}${link('/rates/', 'Get a Quote')}${link('/faq/', 'FAQs')}</div>
        <div><h2>Contact</h2><address>${renderIcon('pin')}${escape(business.address)}<br>${link(call, business.phone, '', 'phone')}${link(`mailto:${business.email}`, business.email, '', 'mail')}</address></div>
      </div>
      <div class="footer-bottom"><span>© Umair Taxi and Limo</span><span>Developed by ${link('https://techsoftsystem.com/', 'TechSoftSystem')}</span></div>
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
      <button class="button button--gold form-submit" ${compact ? '' : 'hidden'}>${renderIcon(compact ? 'calendar' : 'chat')}${compact ? 'Continue to Booking' : 'Continue to WhatsApp'}</button>
      ${compact ? '' : `<p class="form-note">Your journey is confirmed after we agree the details with you. See our ${link('/terms/', 'Booking Terms')} and ${link('/privacy-policy/', 'Privacy Policy')}.</p>
      <noscript><p>Send your journey details directly via ${link(whatsapp, 'WhatsApp')} or ${link(call, 'call us')}.</p></noscript>`}
    </form>
  </section>`;
}

export function contactForm() {
  return `<section class="booking-panel" aria-labelledby="contact-form-title">
    <h2 id="contact-form-title">Send an enquiry</h2>
    <p>Fill in your details, then send your message in WhatsApp or your email app.</p>
    <form method="post" data-contact data-whatsapp="${whatsapp}" data-email="${escape(business.email)}">
      <div class="form-grid">
        <label>Name<input name="name" autocomplete="name" required maxlength="100"></label>
        <label>Email<input name="email" type="email" autocomplete="email" required maxlength="140"></label>
        <label>Phone <span>(optional)</span><input name="phone" type="tel" autocomplete="tel" maxlength="35"></label>
        <label>Subject<select name="subject"><option>General enquiry</option>${serviceOptions.map((option) => `<option>${option}</option>`).join('')}</select></label>
        <label class="full">Message<textarea name="message" rows="5" required maxlength="1000"></textarea></label>
      </div>
      <div class="actions contact-actions" hidden>
        <button class="button button--gold" type="submit" value="whatsapp">${renderIcon('chat')}Continue to WhatsApp</button>
        <button class="button button--dark" type="submit" value="email">${renderIcon('mail')}Open email app</button>
      </div>
      <noscript><p>To send your enquiry, ${link(whatsapp, 'open WhatsApp')} or ${link('mailto:' + business.email, 'email us')}.</p></noscript>
      <p class="form-note">${link('/privacy-policy/', 'Privacy Policy')}</p>
    </form>
  </section>`;
}

export const photoPath = (name) => '/assets/photos/' + (/\.(?:jpg|png)$/.test(name) ? name : name + '.webp');

export function image(name, alt, eager = false, dimensions) {
  const [width, height] = dimensions ?? (
    name === 'cork-coast-drive' ? [1500, 1000] : /-studio\.(?:jpg|png)$/.test(name) ? [1140, 750] : [760, 500]
  );
  const responsive = eager && name === 'cork-coast-drive' ? 'srcset="/assets/photos/cork-coast-drive-small.webp 760w, /assets/photos/cork-coast-drive.webp 1500w" sizes="100vw"' : '';
  return `<img src="${photoPath(name)}" alt="${escape(alt)}" width="${width}" height="${height}" ${eager ? 'fetchpriority="high"' : 'loading="lazy" decoding="async"'} ${responsive}>`;
}

export function tiles(items) {
  return `<div class="tiles">${items.map(([href, title, description, icon, anchor, media]) => `<article class="tile${media ? ' tile--media' : ''}"${anchor ? ` id="${anchor}"` : ''} data-reveal>
    ${media ? image(...media) : ''}
    <div class="tile-copy"><h3>${link(href, title, '', icon)}</h3><p>${escape(description)}</p></div>
  </article>`).join('')}</div>`;
}

export const serviceTiles = (selection = services) => tiles(selection.map(([slug, title, icon, description]) => [servicePath(slug), title, description, icon, '', serviceMedia[slug]]));
export const areaTiles = () => tiles(areas.map(([slug, title, description]) => [areaPath(slug), title, description, 'pin', slug === 'county-cork' ? 'co-cork' : slug, areaMedia[slug]]));
export const process = () => `<ol class="steps">${steps.map(([title, description]) => `<li data-reveal><h3>${title}</h3><p>${description}</p></li>`).join('')}</ol>`;
export const questions = () => `<div class="questions">${faqs.map(([title, answer]) => `<details><summary><span>${renderIcon('question')}${title}</span>${renderIcon('plus')}${renderIcon('minus')}</summary><p>${answer}</p></details>`).join('')}</div>`;
export const section = (title, body, className = '', id = '') => `<section class="section ${className}"${id ? ` id="${id}"` : ''}><div class="shell"><h2 data-reveal>${title}</h2>${body}</div></section>`;

export function journeyFeature(media, title, description, cta) {
  return `<section class="journey-feature shell" aria-labelledby="journey-feature-title">
    <div class="journey-feature-photo" data-reveal>${image(...media)}</div>
    <div class="journey-feature-copy">
      <p class="eyebrow">Why choose us</p>
      <h2 id="journey-feature-title">${escape(title)}</h2>
      <p>${escape(description)}</p>
      ${link(...cta)}
    </div>
  </section>`;
}

export function journeySteps(title, firstStep) {
  const items = [
    ['pin', 'Send the trip details', firstStep],
    ['chat', 'Agree the arrangements', 'We’ll discuss availability, pickup and the quote with you.'],
    ['calendar', 'Meet at the agreed spot', 'Keep the booking confirmation and pickup details handy on the day.'],
  ];
  return section(escape(title), `<ol class="journey-steps">${items.map(([symbol, heading, detail]) => `
    <li><div class="journey-step-icon">${renderIcon(symbol)}</div><h3>${heading}</h3><p>${escape(detail)}</p></li>`).join('')}</ol>`, 'journey-planning');
}

export function tourTiles(selection) {
  return `<div class="tour-grid">${selection.map(([slug, title, description]) => `<article class="tour-card" id="${slug}" data-reveal>
    <div class="tour-card-image">${image(...tourMedia[slug])}</div>
    <div class="tour-card-content"><h3>${link(tourPath(slug), title)}</h3><p>${escape(description)}</p></div>
  </article>`).join('')}</div>`;
}

export function fleet(selection = vehicles) {
  return `<div class="fleet-cards">${selection.map((vehicle) => {
    const [name, alt] = vehicle.card;
    return `<article class="fleet-card">
      <div class="fleet-card-copy"><h3>${escape(vehicle.title)}</h3><p>${escape(vehicle.description)}</p></div>
      ${image(name, alt)}
      <div class="fleet-card-copy fleet-card-details">${fleetFacts(vehicle, true)}
      ${link(fleetPath(vehicle.slug), 'View ' + vehicle.title + ' details', 'button button--gold')}</div>
    </article>`;
  }).join('')}</div>`;
}

export function fleetFacts(vehicle, compact = false) {
  const labels = compact ? ['Passengers', 'Luggage'] : ['Best for', 'Passengers', 'Luggage'];
  return `<dl class="fleet-facts">${vehicle.quickFacts.slice(compact ? 1 : 0).map((value, index) =>
    `<div><dt>${labels[index]}</dt><dd>${escape(value)}</dd></div>`).join('')}</dl>`;
}

export function fleetShowcase() {
  return `<section class="section" id="vehicles" aria-labelledby="fleet-selection-title"><div class="shell">
    <h2 id="fleet-selection-title" data-reveal>Choose your vehicle</h2>
    <p class="section-lead">Capacity figures are estimates. Actual seating and luggage space vary by vehicle and layout.</p>
    ${fleet()}
  </div></section>`;
}

export function fleetDetails(vehicle, booking) {
  const photos = fleetPhotos(vehicle);
  return `<div class="section fleet-gallery-section" id="vehicle-gallery"><div class="shell fleet-detail-grid">
    <section aria-labelledby="fleet-gallery-title">
    <h2 id="fleet-gallery-title">Vehicle gallery</h2>
    <p class="section-lead" id="fleet-gallery-note">${photos.length > 1 ? 'Swipe through the gallery or select a photo to enlarge it.' : 'Select the vehicle photo to enlarge it.'}</p>
    <div class="fleet-gallery" data-gallery>
      <div class="fleet-gallery-track" id="fleet-gallery-track" tabindex="0" role="region" aria-labelledby="fleet-gallery-title" aria-describedby="fleet-gallery-note">
        ${photos.map(([name, alt, label, dimensions], index) => `<figure class="fleet-gallery-slide">
          <a class="fleet-gallery-photo" href="${photoPath(name)}" data-lightbox-index="${index}" aria-label="Enlarge ${label.toLowerCase()} photo">
            ${image(name, alt, false, dimensions)}<span class="fleet-gallery-enlarge" aria-hidden="true">View Larger</span>
          </a><figcaption>${label}</figcaption></figure>`).join('')}
      </div>
      <div class="fleet-gallery-controls" hidden>
        <div class="fleet-gallery-views" role="group" aria-label="Photo view">
          ${photos.map(([name, , label, dimensions], index) => `<button type="button" data-gallery-index="${index}" aria-label="Enlarge ${label.toLowerCase()} from thumbnail"${index === 0 ? ' aria-current="true"' : ''}>${image(name, '', false, dimensions)}</button>`).join('')}
        </div>
        <div class="fleet-gallery-navigation" role="group" aria-label="Gallery navigation">
          <button type="button" data-gallery-step="-1" aria-controls="fleet-gallery-track">Previous</button>
          <span data-gallery-count>1 of ${photos.length}</span>
          <button type="button" data-gallery-step="1" aria-controls="fleet-gallery-track">Next</button>
          <button type="button" data-gallery-play>Pause Slideshow</button>
        </div>
      </div>
      <dialog class="fleet-lightbox" aria-labelledby="fleet-lightbox-title">
        <div class="fleet-lightbox-top"><h3 id="fleet-lightbox-title">Vehicle photos</h3><button type="button" data-lightbox-close autofocus>Close</button></div>
        <figure><img data-lightbox-photo alt=""><figcaption data-lightbox-caption></figcaption></figure>
        <div class="fleet-lightbox-nav"${photos.length === 1 ? ' hidden' : ''}>
          <button type="button" data-lightbox-step="-1">Previous</button>
          <span data-lightbox-count role="status"></span>
          <button type="button" data-lightbox-step="1">Next</button>
        </div>
      </dialog>
    </div>
    </section>
    <div class="fleet-detail-sidebar">
      <section class="fleet-detail-highlights" aria-labelledby="fleet-highlights-title">
        <h2 id="fleet-highlights-title">Vehicle highlights</h2>
        ${fleetFacts(vehicle)}
        <p class="fleet-estimate-note">Typical estimates. Actual capacity varies by vehicle and seating layout.</p>
      </section>
      <section class="fleet-journey-section" aria-labelledby="fleet-journeys-title">
        <h2 id="fleet-journeys-title">Journeys this vehicle suits</h2>
        <ul class="journey-steps">${vehicle.journeys.map(([title, text]) =>
          `<li><h3>${escape(title)}</h3><p>${escape(text)}</p></li>`).join('')}</ul>
      </section>
    </div>
  </div></div>
  ${journeyFeature(['fleet-east-cork-road', 'Illustrative road above the Irish coastline'], 'Plan your journey from Youghal',
    'Share your pickup, group size and luggage when you enquire about a Cork Airport transfer, a local ride or an Ireland tour.',
    [booking, 'Request a Quote', 'button button--gold', 'calendar'])}`;
}

export function home() {
  return `<section class="hero">
    <div class="shell hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Based in Youghal, Ireland</p>
        <h1>Airport Transfers <span>from Youghal</span></h1>
        <p class="hero-intro">Private transfers to and from Cork Airport, with pickups across Cork and Waterford.</p>
        ${link('#booking', 'Get a Quote & Book', 'button button--gold hero-book', 'calendar')}
      </div>
      <figure class="hero-scene">
        <img src="/assets/photos/cork-airport-mercedes-rear.jpg" alt="Black Mercedes-Benz E-Class executive saloon parked beside the curb at Cork Airport" width="1900" height="550" fetchpriority="high">
      </figure>
    </div>
  </section>
  <section class="home-booking section"><div class="shell">${bookingForm(true)}</div></section>
  <section class="section"><div class="shell">
    <h2 data-reveal>Find the right ride</h2>
    ${tiles([
      ['/airport-transfers/', 'Airport Transfers', services[0][3], 'plane'],
      ['/local-taxi-youghal/', 'Local Taxi', services[1][3], 'taxi'],
      ['/tours/', 'Ireland Tours', 'Plan a private trip through Cork, Waterford or further across Ireland.', 'map'],
    ])}
    <p class="section-note">${link('/services/', 'View all services', 'text-link')}</p>
  </div></section>
  <section class="tour-feature" id="tours"><div class="shell feature-grid">
    <figure data-reveal>${image('irish-atlantic-coast', 'Green headlands overlooking the Atlantic on the Irish coast')}</figure>
    <div data-reveal><h2>Tours around Ireland.</h2><p>Start with Cork and Waterford or plan a trip further afield. Explore ideas for Kerry, the west coast, the midlands, Donegal and Northern Ireland, then tell us the route you have in mind.</p>
      <div class="actions">${link('/tours/', 'Browse Tours', 'button button--gold')}${link(tourPath('custom'), 'Custom Tour', 'button button--outline')}</div>
    </div>
  </div></section>
  ${section('Ideas for a day out', tourTiles(tours.filter(([slug]) => ['cork', 'waterford', 'youghal'].includes(slug))))}
  ${section('Popular routes', `<div class="route-list">${routes.map(([pickup, destination]) => {
    const query = new URLSearchParams({ pickup, destination, trip: destination.includes('Airport') ? 'Airport Transfer' : 'Local Taxi' });
    return link(`/book/?${query}`, `${pickup} → ${destination}`, '', destination.includes('Airport') ? 'plane' : 'taxi');
  }).join('')}</div><p class="section-note">Youghal is our base. Our main pickup areas also include Cork, Waterford and Dungarvan.</p><p class="section-note">${link('/service-areas/', 'View all service areas', 'text-link', 'pin')}</p>`)}
  ${section('How it works', process(), 'surface')}
  ${section('Vehicle options', fleet() + `<p class="section-note">${link('/fleet/', 'View Fleet', 'button button--dark')}</p>`, '', 'fleet')}
  ${section('Frequently asked questions', questions(), 'surface', 'faq')}`;
}

export function prose(blocks) {
  return `<div class="copy-blocks">${blocks.map(([title, description]) => `<section><h2>${escape(title)}</h2><p>${escape(description)}</p></section>`).join('')}</div>`;
}
