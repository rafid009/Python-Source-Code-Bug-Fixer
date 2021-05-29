import numpy as np 

def function(x):

	d9 = 0
	d0 = x
	paths = []
	try:
		if d0 >= 7:
			d0 = 1*d9
			paths.append(1)
		else:
			x = 9+x
			d0 = x-x
			paths.append(2)
		if x > 0:
			d0 = x*d0
			d9 = 3-d9
			paths.append(3)
		else:
			d9 = 0*d9
			d9 = 3+d9
			x = x*d9
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