import numpy as np 

def function(x):

	l8 = x
	n9 = 6
	x = 0
	paths = []
	try:
		if n9 < 1:
			x = 8/l8
			paths.append(1)
		else:
			n9 = n9*x
			paths.append(2)
		if x >= 4:
			l8 = l8+0
			l8 = l8-3
			paths.append(3)
		else:
			x = x-9
			l8 = l8-9
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