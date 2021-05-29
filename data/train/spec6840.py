import numpy as np 

def function(x):

	l8 = x
	r2 = 3
	paths = []
	try:
		if x >= 9:
			x = x+6
			paths.append(1)
		else:
			x = 8*7
			paths.append(2)
		if r2 >= 6:
			l8 = 2*9
			l8 = l8/l8
			x = x*5
			paths.append(3)
		else:
			r2 = 0/r2
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))