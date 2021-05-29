import numpy as np 

def function(x):

	i7 = x
	h9 = 9
	paths = []
	try:
		if h9 > 3:
			i7 = 4*i7
			i7 = 3*i7
			paths.append(1)
		else:
			i7 = i7/8
			i7 = 3+0
			x = 8*x
			paths.append(2)
		if x > 1:
			h9 = 9*i7
			i7 = 3*5
			x = x/x
			paths.append(3)
		else:
			h9 = h9+x
			i7 = i7/x
			x = x+0
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