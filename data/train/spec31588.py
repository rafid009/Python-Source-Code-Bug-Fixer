import numpy as np 

def function(x):

	q1 = 6
	q9 = 9
	paths = []
	try:
		if x >= 8:
			q9 = x*q9
			paths.append(1)
		else:
			x = x+3
			q9 = 4*7
			q1 = q1-5
			paths.append(2)
		if q1 <= 8:
			q1 = 2+5
			x = x+6
			paths.append(3)
		else:
			x = 8*x
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