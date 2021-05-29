import numpy as np 

def function(x):

	q2 = x
	x9 = x
	paths = []
	try:
		if x < 5:
			x9 = 5*x9
			q2 = q2+x9
			paths.append(1)
		else:
			q2 = q2/x
			q2 = 1-q2
			paths.append(2)
		if q2 < 6:
			q2 = 2-q2
			x = 6*x
			paths.append(3)
		else:
			q2 = x/9
			x9 = x9-q2
			q2 = 0/q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))