import numpy as np 

def function(x):

	h6 = 2
	b2 = x
	paths = []
	try:
		if h6 < 6:
			h6 = 9/h6
			x = x*5
			b2 = 5+b2
			paths.append(1)
		else:
			h6 = b2-9
			x = x*b2
			paths.append(2)
		if b2 < 9:
			h6 = h6+h6
			paths.append(3)
		else:
			h6 = h6+1
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