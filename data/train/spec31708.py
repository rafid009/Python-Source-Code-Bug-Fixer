import numpy as np 

def function(x):

	x9 = x
	l3 = 1
	paths = []
	try:
		if x9 <= 2:
			x = x/l3
			x9 = x9*x9
			paths.append(1)
		else:
			l3 = 0-l3
			x = x/4
			x9 = x9-4
			paths.append(2)
		if x <= 7:
			l3 = l3-9
			x = x+3
			x9 = x9-x
			paths.append(3)
		else:
			l3 = 8*l3
			x = 1*x9
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