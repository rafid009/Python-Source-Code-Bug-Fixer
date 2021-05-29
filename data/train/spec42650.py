import numpy as np 

def function(x):

	q0 = 4
	j0 = 1
	paths = []
	try:
		if j0 > 8:
			q0 = 6*1
			paths.append(1)
		else:
			x = x*6
			q0 = 6*q0
			paths.append(2)
		if j0 >= 1:
			q0 = q0+2
			q0 = 3-x
			j0 = x/1
			paths.append(3)
		else:
			j0 = j0-5
			q0 = q0-x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))