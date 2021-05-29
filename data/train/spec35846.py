import numpy as np 

def function(x):

	a3 = 5
	o6 = x
	paths = []
	try:
		if x < 3:
			a3 = a3+2
			a3 = 6-a3
			o6 = 7/o6
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if x >= 9:
			x = 4/x
			o6 = x/2
			x = o6-x
			paths.append(3)
		else:
			a3 = 3+a3
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