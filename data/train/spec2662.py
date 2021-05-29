import numpy as np 

def function(x):

	j1 = x
	i9 = 9
	x = x
	paths = []
	try:
		if i9 >= 7:
			j1 = j1-3
			i9 = i9-6
			paths.append(1)
		else:
			i9 = i9*2
			i9 = j1-2
			paths.append(2)
		if j1 >= 6:
			i9 = i9/5
			j1 = j1*j1
			paths.append(3)
		else:
			j1 = 4-j1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))