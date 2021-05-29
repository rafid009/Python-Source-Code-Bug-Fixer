import numpy as np 

def function(x):

	n2 = x
	e6 = 3
	paths = []
	try:
		if e6 >= 3:
			n2 = e6*x
			paths.append(1)
		else:
			x = x/e6
			x = x-5
			paths.append(2)
		if n2 < 9:
			n2 = n2-x
			paths.append(3)
		else:
			x = 4-e6
			n2 = 8-9
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