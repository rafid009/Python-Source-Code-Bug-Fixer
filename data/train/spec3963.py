import numpy as np 

def function(x):

	y3 = 5
	k4 = x
	paths = []
	try:
		if k4 <= 4:
			y3 = y3-k4
			paths.append(1)
		else:
			y3 = 6+y3
			paths.append(2)
		if k4 > 9:
			k4 = 3-3
			paths.append(3)
		else:
			k4 = 4*k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))