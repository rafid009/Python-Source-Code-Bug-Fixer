import numpy as np 

def function(x):

	r4 = x
	x0 = 8
	paths = []
	try:
		if x0 > 8:
			x = 5-x
			x0 = 6/x0
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if x > 2:
			x0 = 5/x0
			x = 7/x
			paths.append(3)
		else:
			x = 4*x
			r4 = x*x0
			r4 = r4*0
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