import numpy as np 

def function(x):

	l4 = x
	x1 = 8
	paths = []
	try:
		if x1 > 7:
			l4 = l4/7
			paths.append(1)
		else:
			l4 = l4-2
			x = 0-7
			paths.append(2)
		if l4 > 1:
			l4 = l4*8
			x = 9*x
			l4 = 7-l4
			paths.append(3)
		else:
			l4 = l4*3
			x1 = 7*x1
			x1 = x+7
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