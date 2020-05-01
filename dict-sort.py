
d= {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
print(d)
print(sorted(list(d)))

print(sorted(list(d.values())))

# Sort dict by value using list comprehension
v = [value for (key, value) in sorted(d.items())]
k = [key for (key, value) in sorted(d.items())]
print(v)
print(k)

	
