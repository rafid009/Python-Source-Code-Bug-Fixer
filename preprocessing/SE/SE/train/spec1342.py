import numpy as np 

def function(x):

	l6 = 3
	l8 = 8
	x = x
	paths = []
	try:
		if l6 > 2:
			l6 = l6*l6
			paths.append(1)
		else:
			l6 = l6/8
			x = 4*x
			l6 = 4/l8
			paths.append(2)
		if l6 <= 4:
			l8 = 5+l8
			l6 = 4/1
			paths.append(3)
		else:
			x = 0/2
			x = x-3
			l6 = l6-9
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