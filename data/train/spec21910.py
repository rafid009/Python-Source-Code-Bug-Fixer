import numpy as np 

def function(x):

	l8 = x
	x7 = x
	paths = []
	try:
		if x < 6:
			l8 = l8*x7
			paths.append(1)
		else:
			x7 = 8+x7
			x7 = x7-3
			x = x-2
			paths.append(2)
		if x <= 4:
			l8 = x+l8
			paths.append(3)
		else:
			l8 = l8/8
			x = x7/8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x7 = l8**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))