import numpy as np 

def function(x):

	q3 = 6
	q2 = 2
	paths = []
	try:
		if q3 < 7:
			q2 = 7*q2
			q3 = q3-8
			paths.append(1)
		else:
			x = 3-q2
			q2 = x-q2
			paths.append(2)
		if q3 <= 0:
			x = 3+x
			x = x+3
			paths.append(3)
		else:
			q3 = q3+1
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