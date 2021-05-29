import numpy as np 

def function(x):

	n7 = x
	x6 = x
	x = x
	paths = []
	try:
		if x6 >= 0:
			n7 = n7*x
			x6 = 4-6
			x6 = x/5
			paths.append(1)
		else:
			x6 = x6*x
			x6 = x6-x
			n7 = n7/x
			paths.append(2)
		if x <= 2:
			x = 1-x
			paths.append(3)
		else:
			n7 = x/x6
			n7 = 9-n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))