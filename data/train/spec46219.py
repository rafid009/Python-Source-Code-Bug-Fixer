import numpy as np 

def function(x):

	x5 = x
	q1 = 7
	paths = []
	try:
		if x5 <= 8:
			x5 = x-q1
			q1 = q1*3
			x5 = x/5
			paths.append(1)
		else:
			x5 = 6-7
			paths.append(2)
		if x < 3:
			q1 = q1*x5
			q1 = q1-9
			x5 = x5+6
			paths.append(3)
		else:
			q1 = 8-q1
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))