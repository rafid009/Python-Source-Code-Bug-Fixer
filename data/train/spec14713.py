import numpy as np 

def function(x):

	v0 = 6
	k4 = x
	paths = []
	try:
		if v0 < 7:
			v0 = k4/9
			v0 = 1-4
			k4 = 7/1
			paths.append(1)
		else:
			v0 = v0-8
			x = x+7
			paths.append(2)
		if k4 >= 0:
			v0 = 1/v0
			x = x+k4
			paths.append(3)
		else:
			v0 = k4-v0
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