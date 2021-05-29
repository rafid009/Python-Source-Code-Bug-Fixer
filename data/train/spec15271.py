import numpy as np 

def function(x):

	r5 = x
	x3 = 6
	paths = []
	try:
		if r5 < 6:
			r5 = 0+6
			x3 = 6/r5
			paths.append(1)
		else:
			r5 = r5+r5
			x = x*4
			paths.append(2)
		if r5 > 5:
			r5 = 8-x3
			r5 = r5+6
			r5 = 9*x3
			paths.append(3)
		else:
			x = 2/x
			x3 = 0+x3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))