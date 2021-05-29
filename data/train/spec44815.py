import numpy as np 

def function(x):

	q1 = 6
	k5 = x
	paths = []
	try:
		if x < 7:
			k5 = k5-q1
			x = 7+k5
			k5 = 2*k5
			paths.append(1)
		else:
			q1 = 5-q1
			paths.append(2)
		if k5 > 6:
			k5 = 2/3
			paths.append(3)
		else:
			x = x+2
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