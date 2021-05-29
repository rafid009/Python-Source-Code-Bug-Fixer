import numpy as np 

def function(x):

	h3 = 5
	b9 = x
	paths = []
	try:
		if x < 4:
			x = 7*x
			b9 = b9-0
			paths.append(1)
		else:
			h3 = h3-3
			x = b9/4
			paths.append(2)
		if b9 <= 7:
			h3 = 2*h3
			x = x/4
			b9 = b9+2
			paths.append(3)
		else:
			h3 = 6*x
			b9 = b9/b9
			b9 = 0/4
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