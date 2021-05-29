import numpy as np 

def function(x):

	d3 = 8
	q2 = 4
	paths = []
	try:
		if d3 > 3:
			q2 = q2-q2
			q2 = 0-d3
			paths.append(1)
		else:
			q2 = q2+q2
			paths.append(2)
		if q2 >= 5:
			q2 = q2*q2
			paths.append(3)
		else:
			q2 = q2/x
			x = 8-2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))