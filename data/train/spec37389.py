import numpy as np 

def function(x):

	x1 = x
	f8 = x
	paths = []
	try:
		if x1 <= 6:
			x = x*2
			x = x1-x1
			x = 2*x
			paths.append(1)
		else:
			x1 = 8-6
			paths.append(2)
		if x > 1:
			x1 = 3-x1
			x = 7-x
			paths.append(3)
		else:
			x = x*x
			x1 = x1-8
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))