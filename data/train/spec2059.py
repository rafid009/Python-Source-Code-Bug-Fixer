import numpy as np 

def function(x):

	q1 = 9
	l4 = 8
	paths = []
	try:
		if q1 <= 2:
			x = x+1
			paths.append(1)
		else:
			q1 = x/q1
			l4 = x*4
			paths.append(2)
		if x < 0:
			l4 = l4/l4
			paths.append(3)
		else:
			q1 = 0*q1
			x = 4/1
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