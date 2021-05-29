import numpy as np 

def function(x):

	x6 = 2
	n0 = x
	paths = []
	try:
		if x <= 8:
			x = x-2
			paths.append(1)
		else:
			n0 = x6*9
			x6 = 3*x
			n0 = x-x
			paths.append(2)
		if x > 9:
			x = x/2
			n0 = 5/8
			x = x/5
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x6 = n0**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))