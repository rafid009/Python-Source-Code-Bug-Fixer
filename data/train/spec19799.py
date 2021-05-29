import numpy as np 

def function(x):

	a9 = x
	r7 = 2
	paths = []
	try:
		if a9 > 3:
			r7 = r7/x
			x = x/2
			paths.append(1)
		else:
			r7 = r7+8
			x = 8/a9
			paths.append(2)
		if a9 <= 2:
			x = 6*3
			paths.append(3)
		else:
			x = 4-x
			r7 = a9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))