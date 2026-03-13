import { Metadata } from 'next';
import dynamic from 'next/dynamic';
import { FilterBar } from '@/components/shops/FilterBar';

const MapContainer = dynamic(
  () => import('@/components/map/MapContainer').then((mod) => mod.MapContainer),
  {
    ssr: false,
    loading: () => <div className="h-[50vh] w-full bg-muted animate-pulse rounded-lg flex items-center justify-center">Chargement de la carte...</div>,
  }
);

export const metadata: Metadata = {
  title: 'MeatStory 44 - Trouvez les meilleures boucheries en Loire-Atlantique',
  description: 'Recherchez les boucheries de qualité (Bio, Label Rouge, Artisan) autour de vous en Loire-Atlantique.',
};

export default function HomePage() {
  return (
    <div className="flex flex-col min-h-screen bg-background">
      <header className="p-4 bg-primary text-white shadow-md">
        <h1 className="text-2xl font-bold">MeatStory 44</h1>
      </header>

      <main className="flex-1 flex flex-col md:flex-row">
        <div className="w-full md:w-1/3 lg:w-1/4 p-4 flex flex-col border-r">
          <FilterBar />
          <div className="mt-4 flex-1 overflow-y-auto">
            {/* Butcher list or other content could go here */}
          </div>
        </div>

        <div className="w-full md:w-2/3 lg:w-3/4 h-[50vh] md:h-[calc(100vh-64px)]">
          <MapContainer />
        </div>
      </main>
    </div>
  );
}