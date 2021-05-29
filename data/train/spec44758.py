import numpy as np 

def function(x):

	d1 = x
	a8 = 2
	paths = []
	try:
		if d1 >= 6:
			d1 = d1*x
			d1 = d1/6
			paths.append(1)
		else:
			a8 = a8*a8
			x = x+4
			x = x/x
			paths.append(2)
		if x > 6:
			d1 = d1+9
			d1 = 7*3
			paths.append(3)
		else:
			x = a8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))