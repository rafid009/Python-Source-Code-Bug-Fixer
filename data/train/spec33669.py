import numpy as np 

def function(x):

	h2 = 5
	u0 = x
	paths = []
	try:
		if u0 >= 6:
			h2 = h2*5
			paths.append(1)
		else:
			h2 = h2+5
			u0 = x+u0
			paths.append(2)
		if x > 6:
			u0 = 2/u0
			x = h2-4
			x = x/5
			paths.append(3)
		else:
			x = x-4
			u0 = x-u0
			x = x/u0
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