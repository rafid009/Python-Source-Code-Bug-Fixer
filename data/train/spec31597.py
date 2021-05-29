import numpy as np 

def function(x):

	x9 = 1
	y5 = x
	paths = []
	try:
		if y5 > 3:
			x9 = 0/5
			x9 = 2-x9
			x = 5-y5
			paths.append(1)
		else:
			y5 = y5*7
			paths.append(2)
		if y5 > 9:
			x9 = x9+x
			y5 = 4-y5
			paths.append(3)
		else:
			x = 0*x9
			y5 = x9-4
			y5 = 6/y5
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		y5 = x9**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))