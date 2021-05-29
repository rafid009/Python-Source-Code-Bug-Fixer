import numpy as np 

def function(x):

	q3 = 2
	y1 = 5
	paths = []
	try:
		if y1 <= 2:
			q3 = x+q3
			paths.append(1)
		else:
			q3 = 9*q3
			x = x+3
			paths.append(2)
		if y1 < 8:
			x = x/6
			y1 = q3*y1
			y1 = y1/x
			paths.append(3)
		else:
			y1 = 6+y1
			y1 = 3/5
			x = x+7
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))