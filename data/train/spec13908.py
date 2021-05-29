import numpy as np 

def function(x):

	d7 = 5
	a3 = 5
	paths = []
	try:
		if a3 >= 7:
			d7 = 2*d7
			x = 2*x
			x = d7-x
			paths.append(1)
		else:
			a3 = 2*5
			x = x-7
			a3 = a3*3
			paths.append(2)
		if x <= 1:
			a3 = 5-6
			d7 = 2+d7
			paths.append(3)
		else:
			d7 = d7/8
			a3 = x+a3
			a3 = d7*a3
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