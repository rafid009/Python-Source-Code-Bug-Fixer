import numpy as np 

def function(x):

	n1 = x
	d6 = x
	x = x
	paths = []
	try:
		if x > 7:
			d6 = n1/d6
			d6 = d6*9
			n1 = 7-n1
			paths.append(1)
		else:
			n1 = 3+n1
			paths.append(2)
		if n1 > 8:
			x = 4*x
			paths.append(3)
		else:
			d6 = 6*d6
			d6 = 8+2
			d6 = 6/d6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))