import numpy as np 

def function(x):

	x0 = 6
	x1 = 6
	paths = []
	try:
		if x >= 0:
			x1 = x1*5
			x0 = x1*6
			paths.append(1)
		else:
			x0 = x0/3
			x = x1*6
			x = 0-x
			paths.append(2)
		if x >= 3:
			x = 4*x
			x1 = 5-x1
			paths.append(3)
		else:
			x0 = x0*0
			x = 4+1
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