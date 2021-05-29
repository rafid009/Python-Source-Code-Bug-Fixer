import numpy as np 

def function(x):

	l6 = 7
	f1 = x
	paths = []
	try:
		if x >= 6:
			l6 = l6-7
			f1 = 8-4
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if x <= 7:
			x = x+x
			paths.append(3)
		else:
			x = 1*x
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