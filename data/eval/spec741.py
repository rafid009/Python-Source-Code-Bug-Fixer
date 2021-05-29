import numpy as np 

def function(x):

	r5 = 7
	e6 = x
	paths = []
	try:
		if x < 1:
			e6 = x-e6
			e6 = 5*e6
			e6 = 3+7
			paths.append(1)
		else:
			e6 = r5*3
			e6 = x+e6
			paths.append(2)
		if e6 < 1:
			r5 = 0/x
			x = x+5
			r5 = r5+7
			paths.append(3)
		else:
			e6 = 9-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))