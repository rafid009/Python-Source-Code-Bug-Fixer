import numpy as np 

def function(x):

	t1 = x
	x5 = x
	paths = []
	try:
		if x <= 8:
			x5 = x5-1
			paths.append(1)
		else:
			x5 = x/x5
			x5 = 1*4
			x = 4-x
			paths.append(2)
		if x5 > 2:
			x5 = 9*x5
			t1 = t1/x5
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))