import numpy as np 

def function(x):

	b4 = 8
	d1 = 2
	paths = []
	try:
		if x <= 1:
			x = 6+x
			paths.append(1)
		else:
			d1 = 3+4
			paths.append(2)
		if x > 4:
			d1 = d1+6
			paths.append(3)
		else:
			x = x-0
			x = 2*x
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