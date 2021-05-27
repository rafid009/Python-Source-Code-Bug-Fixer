import numpy as np 

def function(x):

	q0 = 9
	n0 = x
	paths = []
	try:
		if n0 <= 2:
			q0 = q0/1
			paths.append(1)
		else:
			x = n0/9
			paths.append(2)
		if q0 < 0:
			n0 = 2/5
			x = x-9
			paths.append(3)
		else:
			q0 = 5*6
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))