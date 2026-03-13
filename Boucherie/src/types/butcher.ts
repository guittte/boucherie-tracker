export interface Location {
  lat: number;
  lng: number;
}

export interface OpeningHours {
  day: string;
  open: string;
  close: string;
  closed?: boolean;
}

export interface Butcher {
  id: string;
  name: string;
  address: string;
  city: string;
  zip_code: string;
  location: {
    type: "Point";
    coordinates: [number, number]; // [lng, lat] for PostGIS
  };
  labels: string[];
  phone?: string;
  email?: string;
  website?: string;
  description?: string;
  opening_hours?: OpeningHours[];
  image_url?: string;
  rating: number;
  review_count: number;
  distance?: number; // Calculated on the fly
}