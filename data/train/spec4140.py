import numpy as np 

def function(x):

	k4 = 4
	i6 = 2
	x = x
	paths = []
	try:
		if k4 > 4:
			k4 = k4*6
			paths.append(1)
		else:
			k4 = 9-i6
			i6 = i6-5
			paths.append(2)
		if k4 < 9:
			i6 = i6+3
			paths.append(3)
		else:
			k4 = 6+0
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