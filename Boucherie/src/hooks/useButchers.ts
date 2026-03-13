import { useQuery } from '@tanstack/react-query';
import { butcherService } from '@/services/butcherService';
import { useSearchStore } from '@/store/useSearchStore';

export const useButchers = (lat?: number, lng?: number) => {
  const { radius, selectedLabels, searchQuery } = useSearchStore();

  return useQuery({
    queryKey: ['butchers', lat, lng, radius, selectedLabels, searchQuery],
    queryFn: async () => {
      let butchers = [];
      if (lat && lng) {
        butchers = await butcherService.getButchersByRadius(lat, lng, radius * 1000);
      } else {
        butchers = await butcherService.getAllButchers();
      }

      return butchers.filter((butcher) => {
        const matchesLabels = selectedLabels.length === 0 || 
          selectedLabels.every(label => butcher.labels.includes(label));
        const matchesSearch = !searchQuery || 
          butcher.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
          butcher.city.toLowerCase().includes(searchQuery.toLowerCase());
        
        return matchesLabels && matchesSearch;
      });
    },
    enabled: true,
  });
};