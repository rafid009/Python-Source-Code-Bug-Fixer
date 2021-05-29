import numpy as np 

def function(x):

	y6 = 9
	y5 = x
	x = 0
	paths = []
	try:
		if x >= 7:
			x = 9+x
			y6 = y6+7
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if x <= 8:
			y5 = 5/y5
			y5 = 5-9
			y5 = y5-8
			paths.append(3)
		else:
			y5 = 3/y5
			y6 = y5/y6
			y5 = y5*y6
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y6 = y5**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))