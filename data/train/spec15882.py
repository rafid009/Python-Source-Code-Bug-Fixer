import numpy as np 

def function(x):

	y6 = x
	a7 = 9
	x = 3
	paths = []
	try:
		if x >= 8:
			a7 = a7/8
			paths.append(1)
		else:
			a7 = 4/7
			x = 4*x
			x = 6-x
			paths.append(2)
		if x < 4:
			a7 = a7-9
			a7 = a7+a7
			a7 = a7/2
			paths.append(3)
		else:
			y6 = y6*9
			y6 = 6+8
			x = y6/2
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