import numpy as np 

def function(x):

	q0 = x
	l2 = x
	paths = []
	try:
		if q0 <= 4:
			l2 = x*7
			l2 = l2-q0
			x = 5/x
			paths.append(1)
		else:
			x = q0+x
			paths.append(2)
		if x < 2:
			q0 = q0-l2
			paths.append(3)
		else:
			x = x-0
			l2 = 8+l2
			l2 = 0*4
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