import numpy as np 

def function(x):

	k4 = 5
	v6 = 7
	paths = []
	try:
		if k4 <= 9:
			k4 = 9-k4
			paths.append(1)
		else:
			v6 = k4-7
			x = 3-v6
			paths.append(2)
		if k4 > 0:
			v6 = 5+v6
			k4 = k4*7
			paths.append(3)
		else:
			k4 = 8-k4
			k4 = 4*k4
			v6 = 9+v6
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