import numpy as np 

def function(x):

	k2 = x
	n6 = 9
	paths = []
	try:
		if n6 < 5:
			x = n6/k2
			x = 7/x
			x = x+2
			paths.append(1)
		else:
			x = 7+9
			paths.append(2)
		if x > 6:
			x = 3-n6
			x = x-5
			x = x-7
			paths.append(3)
		else:
			x = 4-x
			x = 0*x
			k2 = 5+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))