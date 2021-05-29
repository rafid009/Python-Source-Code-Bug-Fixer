import numpy as np 

def function(x):

	w3 = x
	q7 = 3
	x = x
	paths = []
	try:
		if q7 > 8:
			w3 = 6-w3
			q7 = 7-4
			paths.append(1)
		else:
			x = q7-5
			x = 0*x
			paths.append(2)
		if x >= 7:
			x = x-w3
			w3 = w3+w3
			q7 = 3/q7
			paths.append(3)
		else:
			q7 = q7-w3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))