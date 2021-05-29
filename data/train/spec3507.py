import numpy as np 

def function(x):

	a8 = x
	d1 = x
	paths = []
	try:
		if a8 >= 2:
			d1 = x*2
			d1 = d1+d1
			a8 = 2*4
			paths.append(1)
		else:
			a8 = 7*a8
			d1 = 4-4
			d1 = 0*d1
			paths.append(2)
		if a8 <= 6:
			a8 = a8-x
			a8 = a8+8
			x = x*6
			paths.append(3)
		else:
			d1 = 6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))