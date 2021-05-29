import numpy as np 

def function(x):

	q0 = 5
	w3 = 0
	paths = []
	try:
		if x > 4:
			x = x/5
			paths.append(1)
		else:
			q0 = q0-q0
			paths.append(2)
		if x < 7:
			q0 = q0/5
			paths.append(3)
		else:
			q0 = 2*q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))