import numpy as np 

def function(x):

	x6 = 8
	b8 = 2
	paths = []
	try:
		if x6 <= 4:
			b8 = 4+6
			b8 = 2*b8
			paths.append(1)
		else:
			b8 = 8+1
			x6 = 6/x
			paths.append(2)
		if x >= 1:
			b8 = x-x
			b8 = 8-2
			paths.append(3)
		else:
			x = x*b8
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