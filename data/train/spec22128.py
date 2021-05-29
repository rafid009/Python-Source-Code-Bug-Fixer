import numpy as np 

def function(x):

	q6 = x
	k4 = 0
	paths = []
	try:
		if q6 < 4:
			x = 5/x
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x >= 2:
			q6 = 3/q6
			q6 = 3+x
			k4 = k4*8
			paths.append(3)
		else:
			q6 = q6+x
			k4 = k4-4
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x = q6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))