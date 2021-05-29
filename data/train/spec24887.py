import numpy as np 

def function(x):

	d5 = x
	a6 = x
	paths = []
	try:
		if a6 > 9:
			x = x/1
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if d5 < 4:
			d5 = d5*a6
			x = x*a6
			a6 = 0-d5
			paths.append(3)
		else:
			x = x-a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))