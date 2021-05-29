import numpy as np 

def function(x):

	k4 = 0
	y3 = x
	paths = []
	try:
		if k4 < 6:
			k4 = 0-2
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if x <= 6:
			x = x*8
			k4 = k4*6
			y3 = 2-6
			paths.append(3)
		else:
			k4 = 2*k4
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))