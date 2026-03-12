"use client";

import { useSearchStore } from '@/store/useSearchStore';
import { LabelBadge } from './LabelBadge';

const availableLabels = ['Bio', 'Label Rouge', 'Artisan', 'AOC', 'Bleu-Blanc-Coeur'];

export const FilterBar = () => {
  const { searchQuery, setSearchQuery, selectedLabels, toggleLabel, radius, setRadius } = useSearchStore();

  return (
    <div className="space-y-6">
      <div className="space-y-2">
        <label htmlFor="search" className="text-sm font-medium">Rechercher une boucherie</label>
        <input
          id="search"
          type="text"
          className="w-full p-2 border border-input rounded-md"
          placeholder="Ex: Nantes, Bio..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </div>

      <div className="space-y-2">
        <label className="text-sm font-medium">Rayon de recherche: {radius} km</label>
        <input
          type="range"
          min="1"
          max="50"
          value={radius}
          onChange={(e) => setRadius(parseInt(e.target.value))}
          className="w-full accent-primary h-2 bg-secondary rounded-lg cursor-pointer"
        />
      </div>

      <div className="space-y-2">
        <label className="text-sm font-medium">Labels</label>
        <div className="flex flex-wrap gap-2">
          {availableLabels.map((label) => (
            <LabelBadge
              key={label}
              label={label}
              isActive={selectedLabels.includes(label)}
              onClick={() => toggleLabel(label)}
            />
          ))}
        </div>
      </div>
    </div>
  );
};