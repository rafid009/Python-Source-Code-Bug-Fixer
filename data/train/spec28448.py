import numpy as np 

def function(x):

	y1 = 1
	q9 = x
	paths = []
	try:
		if x > 4:
			y1 = x+q9
			paths.append(1)
		else:
			y1 = y1+8
			paths.append(2)
		if q9 < 5:
			y1 = y1+y1
			paths.append(3)
		else:
			q9 = 5/q9
			q9 = q9/1
			x = q9-x
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