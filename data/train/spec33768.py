import numpy as np 

def function(x):

	a3 = x
	o6 = x
	paths = []
	try:
		if x <= 6:
			x = o6-x
			a3 = 6-0
			x = x-a3
			paths.append(1)
		else:
			a3 = 8/2
			o6 = x+o6
			a3 = a3/x
			paths.append(2)
		if x >= 8:
			o6 = o6-5
			x = x+7
			x = 3/x
			paths.append(3)
		else:
			x = x*7
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))