import numpy as np 

def function(x):

	q7 = x
	y0 = x
	paths = []
	try:
		if x > 8:
			x = x/1
			x = x+q7
			paths.append(1)
		else:
			y0 = y0/q7
			paths.append(2)
		if y0 >= 2:
			y0 = x-2
			paths.append(3)
		else:
			y0 = 3/q7
			q7 = q7-6
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		q7 = y0**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))