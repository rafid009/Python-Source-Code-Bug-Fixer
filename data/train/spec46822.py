import numpy as np 

def function(x):

	v6 = 6
	y6 = 7
	paths = []
	try:
		if y6 < 8:
			x = v6-x
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if v6 >= 0:
			y6 = x/y6
			paths.append(3)
		else:
			v6 = 1-v6
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))