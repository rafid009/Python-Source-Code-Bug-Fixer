import numpy as np 

def function(x):

	n4 = x
	d9 = 8
	x = x
	paths = []
	try:
		if x < 5:
			d9 = n4/3
			n4 = 5*x
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if n4 < 5:
			n4 = 0-7
			d9 = 1+d9
			n4 = 4*n4
			paths.append(3)
		else:
			n4 = n4/9
			x = x*d9
			d9 = x/d9
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