import numpy as np 

def function(x):

	k5 = 5
	n7 = x
	paths = []
	try:
		if x <= 8:
			x = 0+x
			k5 = 6/9
			n7 = 6-x
			paths.append(1)
		else:
			k5 = k5/k5
			x = 9*n7
			x = 3/x
			paths.append(2)
		if n7 < 6:
			x = 3-x
			paths.append(3)
		else:
			n7 = 2/n7
			n7 = 5/n7
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