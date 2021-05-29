import numpy as np 

def function(x):

	n9 = x
	d0 = x
	paths = []
	try:
		if x <= 1:
			n9 = d0*n9
			d0 = d0+x
			paths.append(1)
		else:
			x = 6*9
			paths.append(2)
		if x > 8:
			x = x*d0
			paths.append(3)
		else:
			x = 7*x
			d0 = d0/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))