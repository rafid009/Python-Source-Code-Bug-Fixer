import numpy as np 

def function(x):

	k4 = x
	u0 = 8
	paths = []
	try:
		if u0 <= 0:
			u0 = 9*k4
			paths.append(1)
		else:
			u0 = x+7
			u0 = x/1
			paths.append(2)
		if u0 >= 2:
			k4 = 4+1
			paths.append(3)
		else:
			u0 = x/3
			x = x-3
			k4 = 6+2
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