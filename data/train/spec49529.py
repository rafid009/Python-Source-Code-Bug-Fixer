import numpy as np 

def function(x):

	e4 = 1
	o6 = x
	paths = []
	try:
		if o6 >= 3:
			x = 5*x
			o6 = 0+e4
			e4 = x*e4
			paths.append(1)
		else:
			e4 = 7+3
			paths.append(2)
		if o6 < 4:
			x = 4-e4
			paths.append(3)
		else:
			o6 = o6/o6
			o6 = o6-6
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