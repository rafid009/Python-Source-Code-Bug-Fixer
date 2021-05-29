import numpy as np 

def function(x):

	x7 = 6
	q9 = 9
	x = x
	paths = []
	try:
		if x7 < 4:
			x = x/7
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if q9 >= 7:
			x7 = 3-x7
			paths.append(3)
		else:
			q9 = 5-x7
			q9 = 2*q9
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