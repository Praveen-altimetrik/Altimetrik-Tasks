# Dictionary of product details

Products ={1:{"prdname":"brush","quantity":1},
2:{"prdid":2,"prdname":"soap","quantity":2},
3:{"prdid":3,"prdname":"washing powder","quantity":1}},

# 1. get() - Retrieves the value for a given key, returns None if key not found
prdid_2 = Products.get(2)

# 2. keys() - Returns a a view of all the keys in the dictionary
keys = Products.keys()

# 3. values() - Returns a view of all the values in the dictionary
values = Products.values()

# 4. update() - Updates the dictionary with a new key-value pair or modifies existing
Products.update({"prdid":4,"prdname":"candle","quantity":1})

# 5.pop() - Removes the key-value pair in for a given key and returns the values
remove_product = Products.pop(2)

# 6. popitem() - Removes and returns the last inserted key-value pair
Last_product = Products.popitem()

# 7. Clear() - removes all the key-values pairs from dictionary
Products.clear()

for item in Products:
    if item.get("prdname")=="brush":
        print(item)