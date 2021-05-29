import numpy as np 

def function(x):

	r9 = 4
	u7 = x
	paths = []
	try:
		if u7 > 8:
			x = 6*x
			r9 = 8/r9
			paths.append(1)
		else:
			u7 = u7/2
			paths.append(2)
		if x >= 9:
			x = 2-r9
			r9 = x+8
			u7 = x/2
			paths.append(3)
		else:
			u7 = 3*u7
			x = 4-x
			u7 = u7+4
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