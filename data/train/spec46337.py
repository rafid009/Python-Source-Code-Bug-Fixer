import numpy as np 

def function(x):

	l6 = x
	q3 = 3
	paths = []
	try:
		if q3 >= 0:
			x = x+8
			paths.append(1)
		else:
			l6 = q3+l6
			paths.append(2)
		if x <= 1:
			l6 = 2+3
			x = x/8
			x = x/2
			paths.append(3)
		else:
			l6 = l6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))