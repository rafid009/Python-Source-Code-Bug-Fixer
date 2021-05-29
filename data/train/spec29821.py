import numpy as np 

def function(x):

	x0 = x
	q3 = x
	paths = []
	try:
		if x >= 5:
			x0 = 0*x0
			q3 = 6/7
			paths.append(1)
		else:
			q3 = q3/q3
			x0 = 5/x0
			x = x-4
			paths.append(2)
		if q3 >= 1:
			q3 = x+9
			x = x*7
			paths.append(3)
		else:
			x0 = x0+2
			q3 = 4*7
			q3 = x+q3
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))