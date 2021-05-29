import numpy as np 

def function(x):

	q9 = x
	x7 = x
	paths = []
	try:
		if q9 <= 2:
			x = x*6
			x = x/6
			paths.append(1)
		else:
			x7 = 2-3
			paths.append(2)
		if x <= 5:
			x7 = 9*5
			x7 = x7-1
			paths.append(3)
		else:
			q9 = 8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))