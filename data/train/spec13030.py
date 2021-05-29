import numpy as np 

def function(x):

	d2 = 7
	a3 = x
	paths = []
	try:
		if x >= 8:
			d2 = 5*5
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if d2 >= 9:
			d2 = d2+0
			d2 = d2-d2
			paths.append(3)
		else:
			x = 9*a3
			a3 = 2/a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))