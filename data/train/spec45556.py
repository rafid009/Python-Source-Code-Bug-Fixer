import numpy as np 

def function(x):

	o5 = x
	e5 = 1
	x = x
	paths = []
	try:
		if x < 9:
			e5 = e5*e5
			o5 = 2*x
			o5 = 2*o5
			paths.append(1)
		else:
			x = 9+x
			o5 = 3+o5
			e5 = 9-e5
			paths.append(2)
		if o5 >= 0:
			o5 = 8/o5
			x = x-7
			x = x+2
			paths.append(3)
		else:
			x = x*7
			x = x+o5
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