import numpy as np 

def function(x):

	k0 = 4
	q1 = 2
	x = x
	paths = []
	try:
		if q1 > 4:
			k0 = k0-4
			q1 = x/q1
			paths.append(1)
		else:
			q1 = q1-2
			paths.append(2)
		if k0 > 3:
			x = 8/x
			paths.append(3)
		else:
			q1 = k0/2
			x = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))