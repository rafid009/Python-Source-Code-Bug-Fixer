import numpy as np 

def function(x):

	k2 = x
	l5 = 6
	paths = []
	try:
		if x >= 7:
			x = l5-5
			paths.append(1)
		else:
			l5 = 0-9
			paths.append(2)
		if x >= 7:
			k2 = k2+7
			l5 = 4*x
			paths.append(3)
		else:
			k2 = k2*x
			l5 = 9*l5
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