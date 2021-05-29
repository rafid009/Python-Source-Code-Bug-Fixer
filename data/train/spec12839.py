import numpy as np 

def function(x):

	x5 = 1
	h2 = x
	paths = []
	try:
		if x5 > 7:
			x = h2-x
			paths.append(1)
		else:
			h2 = h2+x5
			x5 = x5-h2
			paths.append(2)
		if h2 <= 9:
			h2 = 7+h2
			h2 = h2*5
			paths.append(3)
		else:
			x = 2*x
			h2 = h2+h2
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