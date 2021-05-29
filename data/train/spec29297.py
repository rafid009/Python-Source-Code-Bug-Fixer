import numpy as np 

def function(x):

	y6 = x
	y5 = 3
	paths = []
	try:
		if y6 >= 8:
			y5 = 4*y5
			x = y6-x
			y6 = 4+9
			paths.append(1)
		else:
			y6 = y6/6
			y6 = y6/8
			x = 4/x
			paths.append(2)
		if x > 2:
			x = 8/x
			paths.append(3)
		else:
			x = x+y6
			y6 = x-y6
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))