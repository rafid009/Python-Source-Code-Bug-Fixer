import numpy as np 

def function(x):

	f9 = 1
	y6 = x
	paths = []
	try:
		if x < 6:
			x = 5+y6
			paths.append(1)
		else:
			f9 = f9+y6
			paths.append(2)
		if x >= 4:
			f9 = y6+1
			paths.append(3)
		else:
			y6 = f9*x
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