import numpy as np 

def function(x):

	l8 = x
	x2 = 1
	x = x
	paths = []
	try:
		if x2 >= 7:
			l8 = x+l8
			x = x-x
			x2 = x2-l8
			paths.append(1)
		else:
			x2 = x2-l8
			paths.append(2)
		if l8 > 3:
			x = x-0
			paths.append(3)
		else:
			l8 = 1*l8
			x2 = 6*x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))