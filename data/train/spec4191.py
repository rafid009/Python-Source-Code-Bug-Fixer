import numpy as np 

def function(x):

	q1 = 1
	x5 = x
	paths = []
	try:
		if x > 3:
			q1 = 5-q1
			x = 2+x5
			paths.append(1)
		else:
			x5 = 8*x5
			x = 2/q1
			paths.append(2)
		if x5 >= 0:
			x = 8+x
			x = x5+2
			x5 = x5-4
			paths.append(3)
		else:
			x5 = 1/x5
			q1 = 2-q1
			x = q1+x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))