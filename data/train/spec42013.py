import numpy as np 

def function(x):

	x1 = 0
	l6 = x
	paths = []
	try:
		if l6 >= 7:
			x1 = x1-1
			x1 = 1+x1
			paths.append(1)
		else:
			x1 = x1+0
			l6 = 0-l6
			paths.append(2)
		if l6 >= 8:
			x = 0+x
			l6 = 4*6
			paths.append(3)
		else:
			l6 = 5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))