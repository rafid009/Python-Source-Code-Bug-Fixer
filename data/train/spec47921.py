import numpy as np 

def function(x):

	r3 = 6
	x0 = x
	paths = []
	try:
		if r3 >= 6:
			x0 = x0-r3
			x = x+1
			paths.append(1)
		else:
			x0 = x0*r3
			r3 = 5-r3
			x0 = x0-3
			paths.append(2)
		if x0 < 8:
			r3 = x*r3
			r3 = 0-r3
			r3 = r3-x0
			paths.append(3)
		else:
			r3 = r3/r3
			x0 = x0+1
			x0 = 8*5
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