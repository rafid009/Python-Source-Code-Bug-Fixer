import numpy as np 

def function(x):

	d2 = 1
	x1 = x
	paths = []
	try:
		if d2 >= 1:
			x = 3-7
			x = x1-x
			paths.append(1)
		else:
			x = x/x1
			paths.append(2)
		if d2 <= 7:
			x1 = 3+x1
			d2 = 7+6
			d2 = x-d2
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))