import numpy as np 

def function(x):

	q9 = 8
	k2 = x
	paths = []
	try:
		if k2 < 2:
			q9 = 9+7
			paths.append(1)
		else:
			x = x/x
			x = 5/x
			x = x-7
			paths.append(2)
		if x < 0:
			q9 = q9*q9
			paths.append(3)
		else:
			k2 = 0*q9
			x = 3+6
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))