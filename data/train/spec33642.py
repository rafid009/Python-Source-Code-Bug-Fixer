import numpy as np 

def function(x):

	x5 = 3
	r1 = x
	paths = []
	try:
		if r1 >= 9:
			x5 = x5-8
			paths.append(1)
		else:
			x = x*x5
			x = 0-x
			paths.append(2)
		if r1 > 2:
			r1 = x5*3
			paths.append(3)
		else:
			x = 0-x5
			r1 = x5+x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))