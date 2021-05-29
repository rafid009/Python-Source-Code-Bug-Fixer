import numpy as np 

def function(x):

	i9 = 4
	v6 = 6
	paths = []
	try:
		if v6 > 7:
			v6 = v6/4
			paths.append(1)
		else:
			i9 = i9+i9
			i9 = v6/i9
			paths.append(2)
		if v6 > 0:
			i9 = i9+x
			paths.append(3)
		else:
			v6 = i9*9
			i9 = x-3
			i9 = 3-x
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