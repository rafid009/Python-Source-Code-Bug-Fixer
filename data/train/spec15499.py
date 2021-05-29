import numpy as np 

def function(x):

	q0 = x
	y6 = 6
	paths = []
	try:
		if x < 0:
			x = x/6
			x = x-3
			y6 = y6/q0
			paths.append(1)
		else:
			q0 = q0*8
			paths.append(2)
		if y6 <= 5:
			x = 4-x
			paths.append(3)
		else:
			x = x/1
			q0 = 6*q0
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