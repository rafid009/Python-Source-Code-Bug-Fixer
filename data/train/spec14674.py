import numpy as np 

def function(x):

	a2 = x
	x5 = x
	paths = []
	try:
		if x5 <= 1:
			x = 8*x
			paths.append(1)
		else:
			a2 = 3/x
			paths.append(2)
		if x5 <= 9:
			x5 = 6-x5
			x = 3/x
			paths.append(3)
		else:
			x5 = 9/x5
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x5 = a2**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))