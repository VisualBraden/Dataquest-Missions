## 1. Reading CSV files with NumPy ##

import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi_shape = taxi.shape

## 2. Reading CSV files with NumPy Continued ##

taxi = np.genfromtxt("nyc_taxis.csv", delimiter=',', skip_header=1)
taxi_shape = taxi.shape

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

#use boolean operations
a_bool = a < 3
b_bool = (b == 'blue')
c_bool = c > 100

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool,5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[28214,5] = 1
taxi_modified[:,0] = 16
mean_trip_distance_arr = taxi_modified[:,7]
mean_trip_dist = np.mean(mean_trip_distance_arr,axis=0)
taxi_modified[[1800,1801],7] = mean_trip_dist

## 7. Assignment Using Boolean Arrays ##

# this creates a copy of our taxi ndarray
taxi_copy = taxi.copy()
total_amount = taxi_copy[:,13]
total_amount[total_amount<0] = 0