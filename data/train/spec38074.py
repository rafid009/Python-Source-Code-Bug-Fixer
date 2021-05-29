import numpy as np 

def function(x):

	l0 = x
	q6 = x
	paths = []
	try:
		if q6 < 9:
			l0 = 7/l0
			q6 = 7-5
			paths.append(1)
		else:
			l0 = l0+4
			paths.append(2)
		if x >= 4:
			x = x-8
			paths.append(3)
		else:
			x = 5-x
			q6 = x/3
			x = 6/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))