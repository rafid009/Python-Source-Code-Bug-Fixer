import numpy as np 

def function(x):

	r5 = x
	e2 = x
	paths = []
	try:
		if r5 > 0:
			r5 = r5+6
			r5 = r5+5
			paths.append(1)
		else:
			r5 = r5-r5
			r5 = 7-x
			e2 = 5+e2
			paths.append(2)
		if r5 > 4:
			r5 = r5-2
			paths.append(3)
		else:
			r5 = 9-1
			x = x/r5
			x = 5-x
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