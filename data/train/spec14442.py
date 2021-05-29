import numpy as np 

def function(x):

	d8 = x
	e2 = 2
	paths = []
	try:
		if x <= 2:
			x = x+e2
			paths.append(1)
		else:
			x = 7-e2
			paths.append(2)
		if d8 >= 5:
			x = 0/e2
			d8 = d8/e2
			paths.append(3)
		else:
			d8 = d8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))