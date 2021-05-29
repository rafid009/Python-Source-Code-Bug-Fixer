import numpy as np 

def function(x):

	x5 = x
	q6 = x
	paths = []
	try:
		if q6 > 1:
			x = 5/q6
			q6 = x/9
			paths.append(1)
		else:
			x = q6-4
			q6 = q6-5
			paths.append(2)
		if x > 0:
			x5 = x-x5
			q6 = 1/q6
			x = x*4
			paths.append(3)
		else:
			x5 = q6-8
			x5 = q6-0
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		x5 = q6**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))