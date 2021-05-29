import numpy as np 

def function(x):

	q6 = x
	u7 = x
	paths = []
	try:
		if x >= 3:
			x = x-2
			paths.append(1)
		else:
			q6 = q6/q6
			paths.append(2)
		if q6 < 7:
			q6 = 0-7
			x = x-1
			paths.append(3)
		else:
			x = x+6
			x = x-7
			q6 = q6/5
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