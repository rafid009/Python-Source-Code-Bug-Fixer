import numpy as np 

def function(x):

	q1 = 5
	k0 = x
	paths = []
	try:
		if q1 >= 4:
			k0 = k0/3
			q1 = 4-q1
			paths.append(1)
		else:
			k0 = k0-6
			x = x*x
			q1 = 6+4
			paths.append(2)
		if k0 >= 2:
			q1 = q1/6
			q1 = 5/q1
			q1 = q1/3
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		q1 = k0**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))