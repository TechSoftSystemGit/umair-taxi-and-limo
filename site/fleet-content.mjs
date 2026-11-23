export const vehicles = [
  {
    slug: 'saloon-taxi',
    title: 'Saloon taxi',
    description: 'A vehicle category to ask about for local trips and airport transfers with standard luggage.',
    icon: 'taxi',
    quickFacts: ['Local rides and Cork Airport transfers', 'Solo travellers and small parties', 'Standard cases, based on size and number'],
    passengerFit: 'Ask about a saloon if you’re travelling alone or with a small party. Send the total number travelling so we can confirm seating.',
    luggageFit: 'Share the number and size of your cases. Let us know about pushchairs or bulky items so we can check boot space.',
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
    quickFacts: ['Family airport trips, tours and golf', 'Families and groups travelling together', 'Ask about suitcases, pushchairs and golf bags'],
    passengerFit: 'Ask about a people carrier for a family or a group travelling together. We’ll check the seating layout for your party.',
    luggageFit: 'Tell us how many suitcases, pushchairs or golf bags you’re bringing. The available luggage space depends on the seating layout.',
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
    quickFacts: ['Group transfers, tours and events', 'Larger parties travelling together', 'Space depends on the seating layout and bags'],
    passengerFit: 'For a larger party travelling together, send the full headcount so we can confirm a suitable seating layout and availability.',
    luggageFit: 'List suitcases and larger items such as golf bags. We’ll check whether the available configuration has enough room for passengers and luggage.',
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
export const fleetPhotos = (vehicle) => views.map(([angle, label]) => [
  `fleet-${vehicle.slug}-${angle}`, `${label} of an illustrative ${vehicle.title.toLowerCase()}`, label,
]);
