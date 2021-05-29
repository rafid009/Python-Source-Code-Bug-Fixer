import numpy as np 

def function(x):

	q1 = x
	x9 = x
	paths = []
	try:
		if x < 5:
			x = x*5
			paths.append(1)
		else:
			x9 = x9+x9
			q1 = q1+q1
			x9 = 6-0
			paths.append(2)
		if x <= 2:
			q1 = q1-6
			x9 = x/x9
			paths.append(3)
		else:
			q1 = 2-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))