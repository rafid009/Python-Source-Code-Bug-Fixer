import numpy as np 

def function(x):

	i9 = x
	n7 = x
	paths = []
	try:
		if x >= 8:
			x = 7*9
			paths.append(1)
		else:
			i9 = 3+6
			i9 = 7+5
			i9 = i9+n7
			paths.append(2)
		if x >= 7:
			x = 4*x
			i9 = i9+5
			x = 9+5
			paths.append(3)
		else:
			x = 7/x
			i9 = 2+i9
			n7 = 5-n7
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