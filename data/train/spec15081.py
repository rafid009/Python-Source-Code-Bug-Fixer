import numpy as np 

def function(x):

	d4 = 4
	n3 = x
	paths = []
	try:
		if n3 >= 1:
			x = 0+n3
			paths.append(1)
		else:
			x = x*1
			n3 = d4*d4
			paths.append(2)
		if d4 >= 5:
			n3 = d4-n3
			paths.append(3)
		else:
			d4 = 0/x
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