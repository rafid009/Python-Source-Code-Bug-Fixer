import numpy as np 

def function(x):

	a8 = 1
	q7 = x
	paths = []
	try:
		if q7 >= 4:
			a8 = 8+q7
			x = x/6
			q7 = 0-q7
			paths.append(1)
		else:
			a8 = 7*a8
			q7 = 6+a8
			paths.append(2)
		if a8 > 8:
			q7 = q7*a8
			paths.append(3)
		else:
			q7 = q7/8
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))