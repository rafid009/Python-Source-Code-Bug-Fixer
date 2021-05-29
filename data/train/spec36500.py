import numpy as np 

def function(x):

	o2 = x
	x1 = 6
	paths = []
	try:
		if o2 < 0:
			x1 = 3/x1
			x1 = x1+7
			paths.append(1)
		else:
			x1 = 7-x1
			paths.append(2)
		if x1 <= 6:
			x = x/2
			paths.append(3)
		else:
			x1 = 3+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))