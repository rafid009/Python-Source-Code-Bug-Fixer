import numpy as np 

def function(x):

	a6 = 1
	d4 = 8
	paths = []
	try:
		if d4 >= 4:
			d4 = 5-x
			paths.append(1)
		else:
			d4 = d4-2
			x = 4*x
			x = a6+x
			paths.append(2)
		if a6 >= 0:
			a6 = a6/8
			x = 6-x
			a6 = a6+a6
			paths.append(3)
		else:
			d4 = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))