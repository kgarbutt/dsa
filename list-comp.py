# list comprehension in Python

l = [2,4,8,16]

m = [i**3 for i in l]
n = [i*2 for i in l]

print(m)
print(n)

print('#' * 8)

def f1(x):
	return x*2
	
def f2(x):
	return x*4
	
lst = []
for i in range(16):
	lst.append(f1(f2(i)))
	
print(lst)
print([f1(x) for x in range(64) if x in [f2(j) for j in range(16)]])

