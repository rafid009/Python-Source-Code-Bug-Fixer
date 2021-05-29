import numpy as np 

def function(x):

	q3 = 2
	x5 = x
	paths = []
	try:
		if x5 > 5:
			q3 = q3-3
			x5 = x5*x5
			x5 = x5-q3
			paths.append(1)
		else:
			x = 3-x
			x = x/x
			paths.append(2)
		if x5 < 6:
			x = 7*x
			paths.append(3)
		else:
			q3 = q3-8
			q3 = x5/1
			q3 = 4+q3
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