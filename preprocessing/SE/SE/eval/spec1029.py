import numpy as np 

def function(x):

	j8 = 4
	y6 = x
	x = 7
	paths = []
	try:
		if y6 < 1:
			x = 4-x
			j8 = j8+4
			paths.append(1)
		else:
			y6 = y6/y6
			y6 = j8*x
			paths.append(2)
		if x > 4:
			y6 = 9+j8
			y6 = y6-2
			y6 = y6*6
			paths.append(3)
		else:
			j8 = 7/j8
			j8 = 9*j8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))