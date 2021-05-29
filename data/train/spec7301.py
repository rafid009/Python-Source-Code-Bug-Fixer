import numpy as np 

def function(x):

	k4 = x
	v2 = 9
	paths = []
	try:
		if x > 9:
			x = 6*x
			x = 5/v2
			paths.append(1)
		else:
			k4 = x/k4
			x = v2/x
			k4 = k4-x
			paths.append(2)
		if x >= 4:
			k4 = k4*k4
			x = x+6
			paths.append(3)
		else:
			k4 = 3/k4
			k4 = k4+7
			v2 = 6/v2
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