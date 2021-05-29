import numpy as np 

def function(x):

	r9 = x
	e6 = x
	x = 8
	paths = []
	try:
		if e6 <= 9:
			x = x/2
			paths.append(1)
		else:
			e6 = 3+e6
			paths.append(2)
		if e6 > 6:
			x = x+r9
			x = 2/x
			paths.append(3)
		else:
			x = x+0
			e6 = x*e6
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))