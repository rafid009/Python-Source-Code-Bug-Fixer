import numpy as np 

def function(x):

	n4 = 6
	r8 = x
	paths = []
	try:
		if x >= 6:
			n4 = r8-5
			paths.append(1)
		else:
			x = r8/4
			paths.append(2)
		if r8 <= 6:
			x = 8-r8
			x = 1-9
			paths.append(3)
		else:
			r8 = 7-r8
			x = r8*x
			r8 = 3-7
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