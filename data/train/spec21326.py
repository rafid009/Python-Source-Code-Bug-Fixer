import numpy as np 

def function(x):

	y1 = x
	q6 = x
	paths = []
	try:
		if x <= 0:
			x = 9-x
			paths.append(1)
		else:
			x = x*7
			x = y1+x
			q6 = q6+0
			paths.append(2)
		if q6 < 6:
			y1 = 4+9
			paths.append(3)
		else:
			y1 = 3/y1
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		y1 = q6**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))