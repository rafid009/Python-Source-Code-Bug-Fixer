import numpy as np 

def function(x):

	r0 = x
	x7 = x
	paths = []
	try:
		if x7 > 1:
			r0 = 2-r0
			x7 = 9+2
			x7 = x7/9
			paths.append(1)
		else:
			r0 = r0+7
			x7 = 3-x7
			paths.append(2)
		if x7 > 0:
			x7 = x7-7
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))