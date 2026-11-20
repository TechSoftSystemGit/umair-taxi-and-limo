const artwork = {
  plane: '<path d="M12 3a2 2 0 0 0-2 2v5l-7 4v2l7-2v4l-2 2v1l4-1 4 1v-1l-2-2v-4l7 2v-2l-7-4V5a2 2 0 0 0-2-2Z"/>',
  taxi: '<path d="m5 12 2-5h10l2 5M9 7V4h6v3M5 18v2m14-2v2"/><rect x="3" y="12" width="18" height="6" rx="2"/><path d="M7 15h1m8 0h1"/>',
  car: '<path d="m5 12 2-5h10l2 5M5 18v2m14-2v2"/><rect x="3" y="12" width="18" height="6" rx="2"/><path d="M7 15h1m8 0h1"/>',
  golf: '<path d="M12 17V3l7 3-7 3m5 7c2 .5 3 1.2 3 2 0 1.7-3.6 3-8 3s-8-1.3-8-3c0-.8 1-1.5 3-2"/>',
  case: '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V4h8v3M3 12l9 3 9-3"/>',
  health: '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8m-4-4h8"/>',
  bus: '<rect x="4" y="3" width="16" height="16" rx="3"/><path d="M4 12h16M7 19v2m10-2v2m-9-6h1m6 0h1"/>',
  calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4m8-4v4m-8 8h2m3 0h2"/>',
  chat: '<path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5H4l1.6-3.2A8.5 8.5 0 1 1 21 11.5Z"/><path d="M8 12h8"/>',
  phone: '<path d="M21 16v3a2 2 0 0 1-2.2 2A18 18 0 0 1 3 5.2 2 2 0 0 1 5 3h3l2 5-2.4 1.6a13 13 0 0 0 6.8 6.8L16 14l5 2Z"/>',
  mail: '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
  pin: '<path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
  map: '<path d="m3 6 6-3 6 3 6-3v15l-6 3-6-3-6 3Zm6-3v15m6-12v15"/>',
  question: '<circle cx="12" cy="12" r="9"/><path d="M9 9a3 3 0 0 1 6 0c0 2-3 2-3 4m0 3v.1"/>',
  plus: '<path d="M5 12h14m-7-7v14"/>',
  minus: '<path d="M5 12h14"/>',
};

export function icon(name) {
  if (!name) return '';
  if (!Object.hasOwn(artwork, name)) throw new Error('Unknown icon: ' + name);
  return `<svg class="icon" aria-hidden="true" focusable="false" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round">${artwork[name]}</svg> `;
}
