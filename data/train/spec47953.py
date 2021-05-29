import numpy as np 

def function(x):

	x6 = 0
	q9 = 1
	paths = []
	try:
		if x6 >= 6:
			x = 5-x
			paths.append(1)
		else:
			x = q9/x
			paths.append(2)
		if x6 < 3:
			x = x6-x
			q9 = x6/8
			x6 = x6*x6
			paths.append(3)
		else:
			x = x-9
			x = q9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))