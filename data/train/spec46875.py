import numpy as np 

def function(x):

	x4 = 0
	q6 = 0
	paths = []
	try:
		if x4 > 8:
			x4 = x4+q6
			paths.append(1)
		else:
			x = x+3
			x = q6*x
			paths.append(2)
		if x > 6:
			x = 7/9
			paths.append(3)
		else:
			x4 = x4-7
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))