import numpy as np 

def function(x):

	x6 = x
	x = x
	paths = []
	try:
		if x <= 8:
			x = 1/2
			x6 = 3-x6
			paths.append(1)
		else:
			x = 8*x
			x = x6*x
			x = 4-x6
			paths.append(2)
		if x > 3:
			x = 2+3
			x6 = 3/x
			paths.append(3)
		else:
			x6 = 5/x6
			x6 = x6-4
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