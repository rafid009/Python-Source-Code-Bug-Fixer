import numpy as np 

def function(x):

	q0 = x
	q8 = 8
	x = x
	paths = []
	try:
		if q0 <= 7:
			q8 = 3/q8
			q0 = q8-0
			paths.append(1)
		else:
			q8 = q8-1
			q0 = q0*8
			x = x+6
			paths.append(2)
		if x > 6:
			q0 = q0-x
			q0 = q0/q0
			paths.append(3)
		else:
			q0 = q0/5
			x = x+x
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