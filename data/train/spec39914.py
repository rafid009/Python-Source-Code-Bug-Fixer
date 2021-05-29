import numpy as np 

def function(x):

	i9 = x
	q7 = 5
	paths = []
	try:
		if q7 < 7:
			q7 = 7-3
			paths.append(1)
		else:
			x = 4-x
			q7 = 4+q7
			paths.append(2)
		if q7 < 7:
			i9 = i9*3
			x = x+5
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))