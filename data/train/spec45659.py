import numpy as np 

def function(x):

	y6 = 8
	q6 = 6
	paths = []
	try:
		if x < 5:
			y6 = y6*7
			x = 4-x
			paths.append(1)
		else:
			y6 = 5/y6
			paths.append(2)
		if q6 >= 3:
			q6 = q6*0
			y6 = 1-y6
			paths.append(3)
		else:
			y6 = y6/q6
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