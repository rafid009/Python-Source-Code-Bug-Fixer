import numpy as np 

def function(x):

	q6 = 3
	x4 = x
	paths = []
	try:
		if q6 < 4:
			q6 = q6/x
			paths.append(1)
		else:
			x4 = x4+0
			paths.append(2)
		if x >= 1:
			q6 = q6+7
			paths.append(3)
		else:
			x4 = 4-8
			x = x-9
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