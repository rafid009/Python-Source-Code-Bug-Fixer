import numpy as np 

def function(x):

	l2 = 5
	y8 = x
	paths = []
	try:
		if y8 >= 5:
			x = y8+x
			paths.append(1)
		else:
			x = x/8
			y8 = 1/y8
			l2 = x/y8
			paths.append(2)
		if l2 < 6:
			l2 = y8-7
			paths.append(3)
		else:
			y8 = y8+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))