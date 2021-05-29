import numpy as np 

def function(x):

	y0 = 7
	q7 = x
	paths = []
	try:
		if y0 >= 5:
			x = 2+x
			q7 = q7*4
			q7 = q7/9
			paths.append(1)
		else:
			q7 = q7+9
			y0 = y0/x
			x = 2/x
			paths.append(2)
		if q7 <= 6:
			x = 1+x
			x = 8-q7
			x = x+y0
			paths.append(3)
		else:
			q7 = 4*q7
			x = y0*y0
			q7 = 3/q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))