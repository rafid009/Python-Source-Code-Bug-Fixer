import numpy as np 

def function(x):

	q0 = x
	x1 = 8
	paths = []
	try:
		if x1 <= 5:
			q0 = q0-4
			x1 = x1/5
			x = x+8
			paths.append(1)
		else:
			q0 = 2-x1
			q0 = x+7
			paths.append(2)
		if x > 8:
			x = q0+x
			x1 = 8+x1
			paths.append(3)
		else:
			x1 = x1/2
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