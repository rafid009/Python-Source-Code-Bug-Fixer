import numpy as np 

def function(x):

	d9 = x
	a7 = x
	paths = []
	try:
		if x < 8:
			a7 = a7+9
			paths.append(1)
		else:
			a7 = d9+4
			d9 = a7*d9
			paths.append(2)
		if x <= 3:
			a7 = 9-a7
			x = 0-x
			paths.append(3)
		else:
			d9 = d9*a7
			a7 = 9-a7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))