import numpy as np 

def function(x):

	o1 = 5
	l9 = x
	paths = []
	try:
		if o1 > 0:
			l9 = l9*x
			paths.append(1)
		else:
			x = o1-3
			x = 2/x
			paths.append(2)
		if x >= 7:
			x = 3+7
			paths.append(3)
		else:
			o1 = 6-o1
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