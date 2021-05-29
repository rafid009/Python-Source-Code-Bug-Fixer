import numpy as np 

def function(x):

	x6 = x
	n4 = 7
	paths = []
	try:
		if n4 < 0:
			x = 4*n4
			x = x+0
			paths.append(1)
		else:
			x = 9-5
			paths.append(2)
		if n4 < 0:
			x6 = x6/n4
			x = x+4
			x6 = 1-x6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))