sammy = {'username': 'sammy-shark',
         'online': True,
         'followers': 987}

print(sammy)

# dict.keys() isolates keys
keys = sammy.keys()
print(keys)

# dict.values() isolates values
values = sammy.values()
print(values)

# dict.items() returns all of the items a dictionary, in a list format of (key, value) tuple pairs.
items = sammy.items()
print(items)

# dict.keys() can be used to query across dictionaries.
# For example, we can take a look at the common keys shared between two dictionary data structures.
jesse = {'username': 'JOctopus', 'online': False, 'points': 723}
print(jesse)

for common_key in sammy.keys() & jesse.keys():
    print(sammy[common_key], jesse[common_key])
