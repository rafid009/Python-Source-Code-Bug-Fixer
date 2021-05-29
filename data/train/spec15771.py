import numpy as np 

def function(x):

	k6 = x
	a8 = 5
	x = 9
	paths = []
	try:
		if x <= 7:
			x = a8-x
			k6 = 1-k6
			paths.append(1)
		else:
			a8 = 0-x
			a8 = 5-3
			x = x*k6
			paths.append(2)
		if k6 < 5:
			k6 = 8-6
			x = x-9
			paths.append(3)
		else:
			a8 = 5+7
			x = a8*x
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