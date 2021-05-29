import numpy as np 

def function(x):

	y7 = 1
	q6 = x
	x = x
	paths = []
	try:
		if q6 <= 5:
			q6 = q6-4
			x = q6/1
			paths.append(1)
		else:
			y7 = y7/5
			paths.append(2)
		if q6 <= 5:
			q6 = 3*2
			paths.append(3)
		else:
			x = 5/x
			x = x/q6
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