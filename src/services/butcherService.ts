import { supabase } from '@/lib/supabase';
import { Butcher } from '@/types/butcher';

export const butcherService = {
  async getAllButchers(): Promise<Butcher[]> {
    const { data, error } = await supabase
      .from('butchers')
      .select('*');

    if (error) throw error;
    return data || [];
  },

  async getButcherById(id: string): Promise<Butcher | null> {
    const { data, error } = await supabase
      .from('butchers')
      .select('*')
      .eq('id', id)
      .single();

    if (error) throw error;
    return data;
  },

  async getButchersByRadius(lat: number, lng: number, radiusMeters: number): Promise<Butcher[]> {
    const { data, error } = await supabase.rpc('get_butchers_in_radius', {
      lat,
      lng,
      radius_meters: radiusMeters,
    });

    if (error) throw error;
    return data || [];
  },
};