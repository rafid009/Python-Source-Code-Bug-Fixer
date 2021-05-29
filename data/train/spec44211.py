import numpy as np 

def function(x):

	y2 = x
	q9 = 5
	x = 7
	paths = []
	try:
		if y2 < 4:
			q9 = 0*q9
			paths.append(1)
		else:
			y2 = y2/1
			paths.append(2)
		if x > 2:
			q9 = q9-6
			x = x*y2
			paths.append(3)
		else:
			y2 = y2*3
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))