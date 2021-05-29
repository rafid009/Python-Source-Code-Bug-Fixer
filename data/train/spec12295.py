import numpy as np 

def function(x):

	u2 = 7
	q9 = x
	x = x
	paths = []
	try:
		if u2 < 9:
			q9 = 7+5
			paths.append(1)
		else:
			q9 = x-u2
			q9 = 6-q9
			paths.append(2)
		if u2 > 2:
			x = x+x
			u2 = 3/u2
			paths.append(3)
		else:
			u2 = 7/q9
			q9 = 1*q9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))