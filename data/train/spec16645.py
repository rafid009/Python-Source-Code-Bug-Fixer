import numpy as np 

def function(x):

	e0 = x
	q1 = 6
	paths = []
	try:
		if x < 6:
			q1 = 6/q1
			x = 1+x
			paths.append(1)
		else:
			q1 = x+3
			e0 = 1-e0
			x = 8+9
			paths.append(2)
		if q1 < 7:
			q1 = e0*3
			paths.append(3)
		else:
			x = 9+x
			e0 = e0-6
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		q1 = e0**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))