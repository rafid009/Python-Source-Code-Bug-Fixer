import numpy as np 

def function(x):

	q7 = x
	y4 = x
	paths = []
	try:
		if x < 2:
			q7 = 7-1
			y4 = y4-y4
			paths.append(1)
		else:
			y4 = 9+5
			q7 = q7/x
			q7 = q7/4
			paths.append(2)
		if y4 < 4:
			x = 4*x
			y4 = 3-y4
			paths.append(3)
		else:
			x = 8*2
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