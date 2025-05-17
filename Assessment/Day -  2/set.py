# Set of items
numbers = {1,2,3,4,5}

# 1. add() - Adds an element to the set
numbers.add(6)

# 2. remove() - Removes an element from the set
numbers.remove(4)

# 3. discard() - Remove an element, but does not raise an error if not found
numbers.discard(7)

# 4. union() - Returns a set containing all elements from both sets
another_set = {5,6,7,8}
union_set = numbers.union(another_set)

# 5. intersection() - Returns a set containing only common elements
intersection_set = numbers.intersection(another_set)

# 6. clear() - Remove all elements from set
numbers.clear()

print("The final set is:{}".format(numbers))
print("the Union set is:{}".format(union_set))
print("The intersection set is:{}".format(intersection_set))