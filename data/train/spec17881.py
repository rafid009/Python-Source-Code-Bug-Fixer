import numpy as np 

def function(x):

	q6 = x
	l9 = x
	paths = []
	try:
		if q6 > 8:
			x = 5/x
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x < 0:
			x = x-4
			q6 = q6*l9
			paths.append(3)
		else:
			l9 = 2-2
			q6 = q6-l9
			q6 = q6-x
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