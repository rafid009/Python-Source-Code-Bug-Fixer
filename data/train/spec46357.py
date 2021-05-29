import numpy as np 

def function(x):

	d9 = 2
	a6 = 9
	paths = []
	try:
		if a6 > 7:
			x = d9/x
			d9 = d9-2
			a6 = a6/x
			paths.append(1)
		else:
			x = a6-1
			paths.append(2)
		if a6 <= 8:
			a6 = 4/a6
			paths.append(3)
		else:
			x = a6/x
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