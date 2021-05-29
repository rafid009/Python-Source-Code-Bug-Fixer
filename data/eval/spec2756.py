import numpy as np 

def function(x):

	a5 = 2
	d2 = 5
	paths = []
	try:
		if x >= 8:
			x = 1*0
			a5 = a5+x
			paths.append(1)
		else:
			d2 = d2-4
			paths.append(2)
		if x >= 8:
			d2 = x-x
			paths.append(3)
		else:
			a5 = d2-5
			d2 = 3*d2
			a5 = a5+a5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))