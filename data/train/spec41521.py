import numpy as np 

def function(x):

	n9 = 1
	d4 = 7
	paths = []
	try:
		if x > 8:
			d4 = 4+n9
			paths.append(1)
		else:
			x = x+9
			n9 = n9*x
			paths.append(2)
		if d4 < 2:
			n9 = 4/n9
			paths.append(3)
		else:
			n9 = n9+7
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