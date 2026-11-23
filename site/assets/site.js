const header = document.querySelector('.site-header');
const menu = header.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const mobile = matchMedia('(max-width: 1110px)');
const groups = [...navigation.querySelectorAll('details')];
function updateHeader() {
  header.classList.toggle('is-scrolled', window.scrollY > 24);
}
updateHeader();
window.addEventListener('scroll', updateHeader, { passive: true });

function setMenu(open) {
  menu.setAttribute('aria-expanded', String(open));
  navigation.hidden = mobile.matches && !open;
  if (!open) groups.forEach((group) => { group.open = false; });
}
function syncMenu() {
  if (mobile.matches && navigation.contains(document.activeElement)) {
    menu.hidden = false;
    menu.focus();
  } else if (!mobile.matches && document.activeElement === menu) {
    navigation.hidden = false;
    navigation.querySelector('a').focus();
  }
  menu.hidden = !mobile.matches;
  setMenu(false);
}
header.dataset.menuReady = '';
syncMenu();
mobile.addEventListener('change', syncMenu);
menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') === 'false'));

for (const group of groups) {
  group.querySelector('summary').addEventListener('click', () => {
    if (!group.open) groups.filter((item) => item !== group).forEach((item) => { item.open = false; });
  });
}
document.addEventListener('click', (event) => {
  for (const group of groups) if (!group.contains(event.target)) group.open = false;
  if (!header.contains(event.target) && menu.getAttribute('aria-expanded') === 'true') {
    if (navigation.contains(document.activeElement)) menu.focus();
    setMenu(false);
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  const openGroup = groups.find((group) => group.open);
  if (openGroup) {
    openGroup.open = false;
    openGroup.querySelector('summary').focus();
  } else if (menu.getAttribute('aria-expanded') === 'true') {
    setMenu(false);
    menu.focus();
  }
});

const query = new URLSearchParams(location.search);
const today = new Intl.DateTimeFormat('sv-SE', {
  timeZone: 'Europe/Dublin', year: 'numeric', month: '2-digit', day: '2-digit',
}).format();

const contactForm = document.querySelector('[data-contact]');
if (contactForm) {
  const requiredText = ['name', 'message'];
  for (const name of requiredText) {
    contactForm.elements.namedItem(name).addEventListener('input', (event) => event.target.setCustomValidity(''));
  }
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    for (const name of requiredText) {
      const field = contactForm.elements.namedItem(name);
      field.setCustomValidity(field.value.trim() ? '' : 'Please enter a value.');
    }
    if (!contactForm.reportValidity()) return;
    const data = new FormData(contactForm);
    const subject = data.get('subject');
    const phone = data.get('phone').trim();
    const details = [
      'Name: ' + data.get('name').trim(),
      'Email: ' + data.get('email').trim(),
      ...(phone ? ['Phone: ' + phone] : []),
      '',
      data.get('message').trim(),
    ].join('\n');
    if (event.submitter?.value === 'email') {
      const mail = 'mailto:' + contactForm.dataset.email + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(details);
      location.assign(mail);
    } else {
      location.assign(contactForm.dataset.whatsapp + '?text=' + encodeURIComponent('Subject: ' + subject + '\n' + details));
    }
  });
  contactForm.querySelector('.contact-actions').hidden = false;
}

for (const form of document.querySelectorAll('[data-quick-booking], [data-full-booking]')) {
  const fields = form.elements;
  fields.date.min = today;
  if (!form.hasAttribute('data-full-booking')) continue;

  for (const name of ['trip', 'pickup', 'destination', 'date', 'time', 'notes']) {
    const value = query.get(name);
    if (!value) continue;
    if (name === 'trip' && ![...fields.trip.options].some((option) => option.value === value)) continue;
    const field = fields.namedItem(name);
    field.value = value.slice(0, field.maxLength > 0 ? field.maxLength : 160);
  }

  const flight = form.querySelector('[data-flight]');
  function updateFlight() {
    flight.hidden = fields.trip.value !== 'Airport Transfer';
    fields.flight.disabled = flight.hidden;
  }
  fields.trip.addEventListener('change', updateFlight);
  updateFlight();

  const labels = [
    ['trip', 'Trip type'], ['pickup', 'Pickup'], ['destination', 'Destination'],
    ['date', 'Date'], ['time', 'Time (Ireland)'], ['passengers', 'Passengers'],
    ['luggage', 'Luggage'], ['flight', 'Flight number'], ['return', 'Return trip'],
    ['name', 'Name'], ['phone', 'Phone'], ['email', 'Email'], ['notes', 'Notes'],
  ];
  const requiredText = ['pickup', 'destination', 'name', 'phone'];
  for (const name of requiredText) {
    fields.namedItem(name).addEventListener('input', (event) => event.target.setCustomValidity(''));
  }
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    for (const name of requiredText) {
      const field = fields.namedItem(name);
      field.setCustomValidity(field.value.trim() ? '' : 'Please enter a value.');
    }
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const details = labels.flatMap(([name, label]) => {
      const value = data.get(name)?.trim();
      return value ? [label + ': ' + value] : [];
    });
    const message = ['Hello Umair Taxi and Limo, I’d like to enquire about a journey.', '', ...details].join('\n');
    location.assign('https://wa.me/353892646246?text=' + encodeURIComponent(message));
  });
  form.querySelector('.form-submit').hidden = false;
}

for (const gallery of document.querySelectorAll('[data-gallery]')) {
  const track = gallery.querySelector('.fleet-gallery-track');
  const controls = gallery.querySelector('.fleet-gallery-controls');
  const count = gallery.querySelector('[data-gallery-count]');
  const views = [...gallery.querySelectorAll('[data-gallery-index]')];
  const [previous, next] = gallery.querySelectorAll('[data-gallery-step]');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  let active = 0;
  function updateGallery() {
    const index = Math.min(views.length - 1, Math.max(0, Math.round(track.scrollLeft / track.clientWidth)));
    if (index === active) return;
    views[active].removeAttribute('aria-current');
    active = index;
    views[active].setAttribute('aria-current', 'true');
    previous.setAttribute('aria-disabled', String(active === 0));
    next.setAttribute('aria-disabled', String(active === views.length - 1));
    count.textContent = `${active + 1} of ${views.length}`;
  }
  function showPhoto(index) {
    if (index < 0 || index >= views.length) return;
    track.scrollTo({ left: index * track.clientWidth, behavior: reducedMotion.matches ? 'instant' : 'smooth' });
  }
  track.addEventListener('scroll', updateGallery, { passive: true });
  views.forEach((button, index) => button.addEventListener('click', () => showPhoto(index)));
  previous.addEventListener('click', () => showPhoto(active - 1));
  next.addEventListener('click', () => showPhoto(active + 1));
  controls.hidden = false;
}

if ('IntersectionObserver' in window && matchMedia('(prefers-reduced-motion: no-preference)').matches) {
  const targets = document.querySelectorAll('[data-reveal]');
  document.documentElement.classList.add('can-reveal');
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('revealed');
      observer.unobserve(entry.target);
    }
  }, { threshold: 0.05 });
  targets.forEach((target) => observer.observe(target));
}
