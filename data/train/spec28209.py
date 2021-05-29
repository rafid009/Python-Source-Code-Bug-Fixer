import numpy as np 

def function(x):

	d5 = x
	v1 = x
	paths = []
	try:
		if v1 > 2:
			d5 = 3*v1
			paths.append(1)
		else:
			v1 = v1+6
			paths.append(2)
		if d5 >= 6:
			d5 = d5/8
			paths.append(3)
		else:
			x = 6*x
			v1 = 2+8
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