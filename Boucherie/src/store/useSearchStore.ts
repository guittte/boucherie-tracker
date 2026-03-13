import { create } from 'zustand';

interface SearchState {
  searchQuery: string;
  selectedLabels: string[];
  radius: number;
  setSearchQuery: (query: string) => void;
  toggleLabel: (label: string) => void;
  setRadius: (radius: number) => void;
  resetFilters: () => void;
}

export const useSearchStore = create<SearchState>((set) => ({
  searchQuery: '',
  selectedLabels: [],
  radius: 10, // Default 10km
  setSearchQuery: (query) => set({ searchQuery: query }),
  toggleLabel: (label) =>
    set((state) => ({
      selectedLabels: state.selectedLabels.includes(label)
        ? state.selectedLabels.filter((l) => l !== label)
        : [...state.selectedLabels, label],
    })),
  setRadius: (radius) => set({ radius }),
  resetFilters: () => set({ searchQuery: '', selectedLabels: [], radius: 10 }),
}));