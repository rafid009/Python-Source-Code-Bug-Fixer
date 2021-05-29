import numpy as np 

def function(x):

	l8 = x
	k3 = 6
	paths = []
	try:
		if x < 1:
			k3 = 2+l8
			x = 7+l8
			paths.append(1)
		else:
			k3 = k3*6
			paths.append(2)
		if x < 4:
			k3 = 4+k3
			l8 = 9+l8
			k3 = k3+5
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))