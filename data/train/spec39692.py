import numpy as np 

def function(x):

	q4 = x
	x9 = x
	paths = []
	try:
		if x < 1:
			x9 = x9-8
			q4 = q4+9
			paths.append(1)
		else:
			q4 = 8-q4
			paths.append(2)
		if q4 <= 6:
			x9 = 5-2
			paths.append(3)
		else:
			x = 3/x
			x = x/5
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))