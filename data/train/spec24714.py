import numpy as np 

def function(x):

	y0 = x
	b7 = x
	x = x
	paths = []
	try:
		if x < 5:
			x = 0*4
			b7 = b7+y0
			paths.append(1)
		else:
			b7 = b7/9
			paths.append(2)
		if b7 >= 2:
			b7 = b7-9
			paths.append(3)
		else:
			y0 = b7-4
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))