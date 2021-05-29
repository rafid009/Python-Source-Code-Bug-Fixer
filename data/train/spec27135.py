import numpy as np 

def function(x):

	n1 = x
	d4 = x
	paths = []
	try:
		if x <= 3:
			n1 = 0/3
			d4 = d4+n1
			n1 = 9*n1
			paths.append(1)
		else:
			n1 = n1-3
			x = 0-n1
			paths.append(2)
		if x >= 4:
			d4 = d4-3
			n1 = 1*0
			d4 = d4+5
			paths.append(3)
		else:
			d4 = n1-d4
			d4 = 6*d4
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