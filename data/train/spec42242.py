import numpy as np 

def function(x):

	k4 = x
	v6 = 2
	paths = []
	try:
		if x >= 2:
			v6 = v6+7
			x = 6-x
			k4 = 0/k4
			paths.append(1)
		else:
			x = x*k4
			paths.append(2)
		if k4 > 2:
			k4 = 8*k4
			paths.append(3)
		else:
			k4 = k4-8
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