import numpy as np 

def function(x):

	e5 = x
	r9 = 9
	paths = []
	try:
		if e5 > 3:
			r9 = 8+r9
			x = x*e5
			paths.append(1)
		else:
			e5 = 1*2
			r9 = r9/r9
			x = 0-9
			paths.append(2)
		if e5 > 8:
			r9 = r9-r9
			x = x-x
			e5 = 7-e5
			paths.append(3)
		else:
			r9 = r9/3
			r9 = 3-r9
			e5 = e5+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))