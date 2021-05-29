import numpy as np 

def function(x):

	e5 = 8
	d2 = 9
	paths = []
	try:
		if d2 <= 0:
			e5 = e5-e5
			paths.append(1)
		else:
			d2 = x+x
			e5 = 2/d2
			x = 2-x
			paths.append(2)
		if d2 < 5:
			e5 = e5/d2
			e5 = 3+d2
			d2 = e5+6
			paths.append(3)
		else:
			e5 = 0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))