import numpy as np 

def function(x):

	x9 = 5
	k6 = 2
	paths = []
	try:
		if x > 6:
			k6 = 4-4
			paths.append(1)
		else:
			x9 = 9+0
			k6 = 1*k6
			k6 = 6+k6
			paths.append(2)
		if x9 < 6:
			x9 = 6-x9
			x = x/7
			x9 = 6/x9
			paths.append(3)
		else:
			k6 = k6-x
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