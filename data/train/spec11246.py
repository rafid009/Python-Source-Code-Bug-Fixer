import numpy as np 

def function(x):

	q6 = x
	y5 = x
	paths = []
	try:
		if q6 <= 5:
			y5 = x/7
			x = 6*x
			paths.append(1)
		else:
			y5 = 6-5
			q6 = 7+8
			paths.append(2)
		if q6 >= 6:
			x = x-y5
			x = x/9
			paths.append(3)
		else:
			y5 = 4-y5
			q6 = 1-5
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