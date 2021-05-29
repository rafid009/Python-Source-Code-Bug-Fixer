import numpy as np 

def function(x):

	a2 = 7
	q0 = 1
	paths = []
	try:
		if a2 > 3:
			q0 = 5*q0
			q0 = a2/1
			q0 = 0-q0
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if a2 > 8:
			q0 = x-2
			paths.append(3)
		else:
			x = x/2
			x = 8+1
			a2 = 2*a2
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))