import numpy as np 

def function(x):

	e2 = 5
	d7 = x
	paths = []
	try:
		if e2 >= 7:
			d7 = 5-d7
			e2 = 1*e2
			paths.append(1)
		else:
			e2 = d7-e2
			x = e2*x
			paths.append(2)
		if d7 > 1:
			e2 = 2/d7
			paths.append(3)
		else:
			e2 = e2+e2
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