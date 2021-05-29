import numpy as np 

def function(x):

	e2 = x
	d8 = x
	paths = []
	try:
		if e2 >= 8:
			e2 = 2/e2
			paths.append(1)
		else:
			x = 4*e2
			paths.append(2)
		if e2 > 7:
			x = e2+x
			paths.append(3)
		else:
			e2 = 9*e2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))