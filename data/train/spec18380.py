import numpy as np 

def function(x):

	e0 = 9
	d1 = 8
	paths = []
	try:
		if d1 >= 6:
			e0 = d1+e0
			paths.append(1)
		else:
			d1 = 1+d1
			paths.append(2)
		if d1 >= 3:
			e0 = e0*x
			e0 = e0/9
			paths.append(3)
		else:
			e0 = e0+0
			e0 = 8+1
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