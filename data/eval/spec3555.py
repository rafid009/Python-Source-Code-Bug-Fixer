import numpy as np 

def function(x):

	u7 = x
	d0 = x
	paths = []
	try:
		if x <= 8:
			u7 = 9*d0
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x >= 8:
			d0 = d0+3
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))