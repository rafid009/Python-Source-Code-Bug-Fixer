import numpy as np 

def function(x):

	l6 = x
	x3 = x
	x = 7
	paths = []
	try:
		if l6 < 4:
			x = l6*x
			l6 = 7+l6
			l6 = x-3
			paths.append(1)
		else:
			l6 = 5-0
			x3 = x3-x
			x3 = x3-0
			paths.append(2)
		if x <= 0:
			x3 = 8+0
			x3 = 2/x3
			x = x-2
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))