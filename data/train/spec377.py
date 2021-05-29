import numpy as np 

def function(x):

	h1 = 6
	j9 = 6
	paths = []
	try:
		if j9 >= 5:
			x = 8*x
			x = 0-x
			j9 = x/j9
			paths.append(1)
		else:
			h1 = j9+6
			paths.append(2)
		if j9 > 1:
			h1 = 7-h1
			j9 = 4-h1
			paths.append(3)
		else:
			x = 1*x
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