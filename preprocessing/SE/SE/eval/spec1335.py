import numpy as np 

def function(x):

	b8 = 8
	h9 = 8
	paths = []
	try:
		if b8 > 1:
			b8 = 8/4
			paths.append(1)
		else:
			x = x-6
			b8 = b8+x
			b8 = b8/1
			paths.append(2)
		if h9 < 1:
			b8 = b8/b8
			b8 = h9*b8
			paths.append(3)
		else:
			x = x-0
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