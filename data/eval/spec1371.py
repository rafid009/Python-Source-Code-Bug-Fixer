import numpy as np 

def function(x):

	y4 = x
	x0 = x
	paths = []
	try:
		if x0 >= 1:
			x0 = x0*y4
			paths.append(1)
		else:
			y4 = y4+y4
			x0 = 8*2
			x = 9+y4
			paths.append(2)
		if y4 > 8:
			x = x/2
			paths.append(3)
		else:
			y4 = x-3
			x0 = x0*2
			y4 = y4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))