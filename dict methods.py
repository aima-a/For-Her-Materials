# Dictionary Methods

dict1 = {"name": "John", "age": 20, "city": "New York"}

# Get value for key
print(dict1.get("name"))

# Get all keys
print(dict1.keys())

# Get all values
print(dict1.values())

# Get key-value pairs
print(dict1.items())

# Check if key exists
print("name" in dict1)

# Add/update key-value pair
dict1["email"] = "john@email.com"

# Remove key-value pair
dict1.pop("age")

# Clear dictionary
dict1.clear()

# Copy dictionary
dict2 = dict1.copy()

# Merge dictionaries
dict1.update(dict2)