import numpy as np 

def function(x):

	j3 = x
	y6 = x
	paths = []
	try:
		if y6 <= 9:
			y6 = 9*y6
			y6 = y6-3
			paths.append(1)
		else:
			y6 = 9+8
			y6 = 5*x
			paths.append(2)
		if x > 6:
			j3 = 6+j3
			paths.append(3)
		else:
			x = y6*x
			y6 = y6+y6
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