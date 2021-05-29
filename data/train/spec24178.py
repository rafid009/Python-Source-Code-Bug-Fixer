import numpy as np 

def function(x):

	y6 = x
	u0 = 6
	paths = []
	try:
		if u0 > 9:
			y6 = y6/8
			u0 = u0/4
			x = 9*x
			paths.append(1)
		else:
			u0 = 4-u0
			u0 = 6-x
			paths.append(2)
		if x <= 8:
			x = 9+x
			paths.append(3)
		else:
			y6 = 4+9
			u0 = u0-x
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