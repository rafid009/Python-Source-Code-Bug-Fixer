import numpy as np 

def function(x):

	g5 = x
	k4 = 6
	paths = []
	try:
		if x < 8:
			x = x/6
			k4 = x/6
			paths.append(1)
		else:
			g5 = 6-g5
			paths.append(2)
		if x < 8:
			x = 0+x
			g5 = 7*9
			k4 = 6+k4
			paths.append(3)
		else:
			g5 = 9/g5
			x = 9-x
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