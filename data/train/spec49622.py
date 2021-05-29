import numpy as np 

def function(x):

	r2 = 3
	d6 = 6
	x = x
	paths = []
	try:
		if d6 >= 3:
			r2 = x+r2
			paths.append(1)
		else:
			d6 = d6*x
			paths.append(2)
		if x < 0:
			x = x-8
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))