import numpy as np 

def function(x):

	q6 = x
	y8 = x
	paths = []
	try:
		if q6 < 3:
			y8 = y8/1
			x = 5-x
			paths.append(1)
		else:
			y8 = y8/x
			paths.append(2)
		if q6 >= 7:
			y8 = 3*2
			y8 = 5*6
			x = q6*3
			paths.append(3)
		else:
			x = x-2
			q6 = q6+5
			y8 = x/y8
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		y8 = q6**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))