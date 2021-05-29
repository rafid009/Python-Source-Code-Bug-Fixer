import numpy as np 

def function(x):

	x8 = x
	q9 = 6
	paths = []
	try:
		if x8 > 9:
			x = 3*x
			x8 = x8/q9
			x8 = x-x8
			paths.append(1)
		else:
			q9 = 8+q9
			paths.append(2)
		if x <= 5:
			x = 2*x
			x = 0-x
			q9 = q9/1
			paths.append(3)
		else:
			q9 = x8/1
			x8 = x8*7
			q9 = 1*q9
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))