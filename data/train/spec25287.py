import numpy as np 

def function(x):

	q6 = 3
	y1 = x
	paths = []
	try:
		if x >= 0:
			q6 = q6*q6
			paths.append(1)
		else:
			q6 = q6*8
			x = 3-x
			q6 = q6-x
			paths.append(2)
		if q6 > 4:
			q6 = q6+0
			paths.append(3)
		else:
			x = 9+1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))