import numpy as np 

def function(x):

	k2 = x
	y6 = 4
	paths = []
	try:
		if y6 > 6:
			y6 = x-x
			paths.append(1)
		else:
			k2 = 0*x
			paths.append(2)
		if y6 <= 4:
			y6 = x/4
			x = 6/x
			paths.append(3)
		else:
			x = x+8
			y6 = y6*9
			x = 6*8
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