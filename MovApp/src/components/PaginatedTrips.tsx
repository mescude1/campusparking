import { useState, useEffect } from 'react';
import { View, Text, FlatList, ActivityIndicator } from 'react-native';

const PAGE_SIZE = 10;

type Trip = {
  id: string;
  date: string;
  driver: string;
  price: string;
};

// Mock function to simulate fetching paginated trips from an API
const fetchTrips = (page: number): Promise<Trip[]> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const newTrips = Array.from({ length: PAGE_SIZE }, (_, index) => ({
        id: `${page * PAGE_SIZE + index + 1}`,
        date: `2024-04-${((index % 30) + 1).toString().padStart(2, '0')}`,
        driver: `Driver ${page * PAGE_SIZE + index + 1}`,
        price: `$${(Math.random() * 200 + 50).toFixed(2)}`,
      }));
      resolve(newTrips);
    }, 1000); // Simulate network delay
  });
};

const PaginatedTrips = () => {
  const [trips, setTrips] = useState<Trip[]>([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  useEffect(() => {
    loadTrips();
  }, []);

  const loadTrips = async () => {
    if (loading || !hasMore) return;

    setLoading(true);
    const newTrips = await fetchTrips(page);
    setTrips((prevTrips) => [...prevTrips, ...newTrips]);
    setPage((prevPage) => prevPage + 1);
    setHasMore(newTrips.length === PAGE_SIZE);
    setLoading(false);
  };

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 18, fontWeight: 'bold', marginBottom: 10 }}>Latest Trips</Text>

      <FlatList
        data={trips}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{ padding: 10, borderBottomWidth: 1, borderBottomColor: '#ddd' }}>
            <Text style={{ fontSize: 16 }}>{item.date}</Text>
            <Text style={{ color: 'gray' }}>Driver: {item.driver}</Text>
            <Text style={{ fontWeight: 'bold' }}>Price: {item.price}</Text>
          </View>
        )}
        onEndReached={loadTrips}
        onEndReachedThreshold={0.1}
        ListFooterComponent={loading ? <ActivityIndicator size="small" color="#007bff" /> : null}
      />
    </View>
  );
};

export default PaginatedTrips;
