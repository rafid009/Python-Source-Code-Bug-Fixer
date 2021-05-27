import numpy as np 

def function(x):

	l2 = 3
	y7 = 9
	paths = []
	try:
		if x > 5:
			x = 7/x
			y7 = 3-x
			x = 5-x
			paths.append(1)
		else:
			l2 = 5/l2
			paths.append(2)
		if x < 3:
			l2 = x-5
			y7 = 8/5
			paths.append(3)
		else:
			y7 = y7-9
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))