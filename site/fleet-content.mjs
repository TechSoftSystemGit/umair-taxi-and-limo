export const vehicles = [
  {
    slug: 'saloon-taxi',
    title: 'Saloon taxi',
    description: 'A vehicle category to ask about for local trips and airport transfers with standard luggage.',
    icon: 'taxi',
    quickFacts: ['Local rides and Cork Airport transfers', 'Up to 4', 'About 2 medium suitcases'],
    journeys: [
      ['Local taxi rides', 'A straightforward option to ask about for trips around Youghal, appointments or going out for dinner.'],
      ['Cork Airport transfers', 'Tell us your flight details and bag count so we can check the vehicle suits the trip.'],
      ['Meetings and events', 'Enquire about travel between your hotel, meeting venue and the airport.'],
    ],
  },
  {
    slug: 'people-carrier',
    title: 'MPV / people carrier',
    description: 'Discuss a people carrier for family airport trips and private tours with extra bags.',
    icon: 'car',
    quickFacts: ['Family airport trips, tours and golf', '5–7', 'About 3–4 medium suitcases'],
    journeys: [
      ['Family airport trips', 'Enquire about room for everyone and ask how your luggage will fit alongside the seats you need.'],
      ['Private tours', 'Share the number of people travelling and the stops you want to make.'],
      ['Golf trips', 'Include the number of club bags and cases when you ask about transfers.'],
    ],
  },
  {
    slug: 'group-vehicle',
    title: 'Large group vehicle',
    description: 'Enquire about transport for a group tour, corporate event or airport trip with several passengers.',
    icon: 'bus',
    quickFacts: ['Group transfers, tours and events', '8–16', 'About 4–8 medium suitcases'],
    journeys: [
      ['Group airport pickups', 'Share your flight plans, arrival point and total luggage for the group.'],
      ['Corporate travel', 'Ask about carrying a group between accommodation, meeting venues and events.'],
      ['Private group tours', 'Send your itinerary ideas and let us know how many people will be travelling together.'],
    ],
  },
];

const views = [
  ['front', 'Front exterior'],
  ['side', 'Side exterior'],
  ['rear', 'Rear exterior'],
  ['interior', 'Passenger interior'],
];

export const fleetPath = (slug) => `/fleet/${slug}/`;
export const fleetHero = (vehicle) => [
  `fleet-${vehicle.slug}-coast`, `Illustrative ${vehicle.title.toLowerCase()} beside the Irish coast`,
];
export const fleetPhotos = (vehicle) => views.map(([angle, label]) => [
  `fleet-${vehicle.slug}-${angle}`, `${label} of an illustrative ${vehicle.title.toLowerCase()}`, label,
]);
