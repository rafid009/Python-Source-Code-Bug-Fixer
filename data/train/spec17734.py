import numpy as np 

def function(x):

	b2 = x
	x3 = 9
	paths = []
	try:
		if x < 1:
			x3 = x3/9
			x = 1/x3
			paths.append(1)
		else:
			x3 = b2/8
			x = x-5
			paths.append(2)
		if x >= 3:
			x = x3*x
			x = 6/x
			paths.append(3)
		else:
			x = x*x
			x = x-9
			x3 = 6/1
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))