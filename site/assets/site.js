const header = document.querySelector('.site-header');
const menu = header.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const mobile = matchMedia('(max-width: 1050px)');
const groups = [...navigation.querySelectorAll('details')];

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

for (const form of document.querySelectorAll('[data-quick-booking], [data-full-booking]')) {
  const fields = form.elements;
  fields.date.min = today;
  if (!form.hasAttribute('data-full-booking')) continue;

  for (const name of ['trip', 'pickup', 'destination', 'date', 'time']) {
    const value = query.get(name);
    if (!value) continue;
    if (name === 'trip' && ![...fields.trip.options].some((option) => option.value === value)) continue;
    fields.namedItem(name).value = value.slice(0, 160);
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
