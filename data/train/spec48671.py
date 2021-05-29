import numpy as np 

def function(x):

	b3 = x
	h1 = x
	paths = []
	try:
		if h1 <= 2:
			b3 = b3*8
			x = x+3
			paths.append(1)
		else:
			h1 = 8*h1
			paths.append(2)
		if h1 <= 4:
			b3 = x-8
			paths.append(3)
		else:
			x = x*1
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