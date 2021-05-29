import numpy as np 

def function(x):

	x5 = 8
	q3 = 6
	paths = []
	try:
		if q3 <= 6:
			q3 = x5+4
			paths.append(1)
		else:
			q3 = x*q3
			x5 = x5*5
			q3 = 4/q3
			paths.append(2)
		if x <= 3:
			q3 = q3*4
			q3 = 4-q3
			paths.append(3)
		else:
			x = q3-q3
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))