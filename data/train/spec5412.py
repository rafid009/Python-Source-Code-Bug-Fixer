import numpy as np 

def function(x):

	e0 = x
	d1 = 5
	x = 9
	paths = []
	try:
		if e0 >= 9:
			d1 = 8+d1
			e0 = 4/e0
			paths.append(1)
		else:
			d1 = 3*x
			paths.append(2)
		if x >= 9:
			d1 = 1+d1
			paths.append(3)
		else:
			d1 = 8/2
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))