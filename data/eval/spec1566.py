import numpy as np 

def function(x):

	e4 = x
	l6 = 7
	paths = []
	try:
		if x >= 6:
			l6 = l6-l6
			l6 = l6+x
			paths.append(1)
		else:
			x = e4+3
			paths.append(2)
		if x <= 2:
			x = 3-l6
			x = e4+4
			x = 8+x
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))