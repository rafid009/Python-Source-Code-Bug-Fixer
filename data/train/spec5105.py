import numpy as np 

def function(x):

	i9 = 3
	w9 = x
	paths = []
	try:
		if x > 0:
			i9 = w9+i9
			i9 = i9-6
			x = 1+x
			paths.append(1)
		else:
			i9 = 0+w9
			x = 4*x
			paths.append(2)
		if x > 7:
			x = x+1
			w9 = w9*3
			x = x-4
			paths.append(3)
		else:
			x = 5+x
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