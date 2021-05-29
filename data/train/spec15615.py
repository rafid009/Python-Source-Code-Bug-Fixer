import numpy as np 

def function(x):

	x7 = x
	r8 = 8
	paths = []
	try:
		if x > 0:
			x = 8+x7
			paths.append(1)
		else:
			x7 = x7*r8
			paths.append(2)
		if r8 < 8:
			x7 = x7/r8
			x7 = x7*4
			paths.append(3)
		else:
			r8 = 6/r8
			r8 = r8-x7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))