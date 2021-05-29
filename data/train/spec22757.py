import numpy as np 

def function(x):

	y4 = 3
	q7 = x
	paths = []
	try:
		if q7 < 2:
			x = 0/6
			paths.append(1)
		else:
			x = 4-q7
			x = x*5
			y4 = 9/y4
			paths.append(2)
		if y4 >= 3:
			x = y4*x
			q7 = q7+8
			paths.append(3)
		else:
			q7 = q7-6
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		y4 = q7**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))