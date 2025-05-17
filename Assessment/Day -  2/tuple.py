#tuple of items

coordinates = (40.7128, -74.0060, 40.7128)

# 1. count() - Count occurrences of a value
count_latitude = coordinates.count(40.7128)

# 2. index() - Returns the index of the first occurrence of a value
index_of_latitude = coordinates.index(40.7128)

print("Count of latitude: {}".format(count_latitude))
print("Index of latitude:{}".format(index_of_latitude))