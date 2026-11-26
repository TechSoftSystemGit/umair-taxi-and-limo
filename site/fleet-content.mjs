export const vehicles = [
  {
    slug: 'saloon-taxi',
    title: 'Executive Saloon Plus',
    description: 'Mercedes-Benz S-Class executive saloon with extended comfort for airport transfers and business travel.',
    card: ['fleet-executive-saloon-studio.jpg', 'Black Mercedes-Benz S-Class executive saloon', 'Exterior'],
    icon: 'taxi',
    quickFacts: ['Airport transfers and executive travel', 'Up to 2', 'Up to 4 bags'],
    journeys: [
      ['Local taxi rides', 'A straightforward option to ask about for trips around Youghal, appointments or going out for dinner.'],
      ['Cork Airport transfers', 'Tell us your flight details and bag count so we can check the vehicle suits the trip.'],
      ['Meetings and events', 'Enquire about travel between your hotel, meeting venue and the airport.'],
    ],
  },
  {
    slug: 'people-carrier',
    title: 'Luxury MPV',
    description: 'Mercedes-Benz V-Class luxury people carrier for family airport trips and private tours.',
    card: ['fleet-luxury-mpv-studio.jpg', 'Black Mercedes-Benz V-Class luxury MPV', 'Exterior'],
    icon: 'car',
    quickFacts: ['Family airport trips, tours and golf', 'Up to 7', 'Up to 7 bags'],
    journeys: [
      ['Family airport trips', 'Enquire about room for everyone and ask how your luggage will fit alongside the seats you need.'],
      ['Private tours', 'Share the number of people travelling and the stops you want to make.'],
      ['Golf trips', 'Include the number of club bags and cases when you ask about transfers.'],
    ],
  },
  {
    slug: 'group-vehicle',
    title: 'Luxury Sprinter Van',
    description: 'Mercedes-Benz Sprinter luxury van for larger groups, airport transfers and corporate events.',
    card: ['fleet-luxury-sprinter-studio.jpg', 'Black Mercedes-Benz Sprinter luxury van', 'Exterior'],
    icon: 'bus',
    quickFacts: ['Group transfers, tours and events', 'Up to 12', 'Up to 12 bags'],
    journeys: [
      ['Group airport pickups', 'Share your flight plans, arrival point and total luggage for the group.'],
      ['Corporate travel', 'Ask about carrying a group between accommodation, meeting venues and events.'],
      ['Private group tours', 'Send your itinerary ideas and let us know how many people will be travelling together.'],
    ],
  },
  {
    slug: '8-seater-taxi',
    title: '8-Seater Taxi',
    description: 'Our Ford 8-seater taxi for group airport transfers, family trips and private day tours.',
    icon: 'taxi',
    card: ['fleet-eight-seater-card-studio.jpg', 'Grey Ford 8-seater taxi with taxi livery', 'Vehicle profile'],
    quickFacts: ['Group airport transfers and private tours', 'Up to 8', 'Varies by bag size and seating'],
    photos: [
      ['fleet-eight-seater-side.jpg', 'Side view of the grey Ford 8-seater taxi', 'Side exterior', [1179, 664]],
      ['fleet-eight-seater-front.jpg', 'Ford taxi parked outside an ivy-covered building', 'Front exterior', [765, 1020]],
      ['fleet-eight-seater-hotel.jpg', 'Ford taxi outside The Montenotte', 'Hotel pickup', [387, 516]],
      ['fleet-eight-seater-interior.jpg', 'Passenger seating in the Ford taxi', 'Passenger interior', [765, 1020]],
      ['fleet-eight-seater-luggage', 'Suitcases loaded in the rear luggage compartment', 'Luggage compartment', [765, 1020]],
    ],
    journeys: [
      ['Airport transfers', 'Share your flight details, passenger count and suitcase sizes so we can check the load before pickup.'],
      ['Private day tours', 'Tell us your starting point and the places your group wants to visit.'],
      ['Hotel and event pickups', 'Arrange travel between your accommodation, venue and return pickup point.'],
    ],
  },
];

export const fleetPath = (slug) => `/fleet/${slug}/`;
export const fleetHero = (vehicle) => vehicle.card.slice(0, 2);
export const fleetPhotos = (vehicle) => vehicle.photos || [vehicle.card];
