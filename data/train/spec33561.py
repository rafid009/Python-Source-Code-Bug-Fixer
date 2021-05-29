import numpy as np 

def function(x):

	q3 = 8
	y6 = 3
	paths = []
	try:
		if x < 6:
			y6 = y6+1
			q3 = y6*5
			paths.append(1)
		else:
			q3 = 7+3
			q3 = 1+2
			y6 = 0+y6
			paths.append(2)
		if x >= 2:
			x = y6+y6
			q3 = q3*6
			paths.append(3)
		else:
			x = x+9
			x = y6-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))