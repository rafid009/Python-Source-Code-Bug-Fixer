import numpy as np 

def function(x):

	l5 = x
	x1 = x
	paths = []
	try:
		if x >= 0:
			x = x*4
			l5 = 6-3
			l5 = x-l5
			paths.append(1)
		else:
			l5 = 4-l5
			paths.append(2)
		if l5 > 9:
			x = 2/x
			x1 = 6*l5
			l5 = 8/x
			paths.append(3)
		else:
			x1 = l5*4
			x1 = 7-x1
			x = x1+7
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