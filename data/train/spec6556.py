import numpy as np 

def function(x):

	q2 = 5
	y2 = 6
	paths = []
	try:
		if x < 7:
			q2 = q2*1
			paths.append(1)
		else:
			y2 = y2-x
			paths.append(2)
		if q2 >= 5:
			x = 2*x
			q2 = 5-q2
			paths.append(3)
		else:
			q2 = 0*q2
			x = x*6
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))