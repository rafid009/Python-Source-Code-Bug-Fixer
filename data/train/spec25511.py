import numpy as np 

def function(x):

	l7 = 4
	q4 = 3
	paths = []
	try:
		if l7 > 1:
			q4 = 0*q4
			paths.append(1)
		else:
			q4 = 1+q4
			l7 = l7+8
			paths.append(2)
		if q4 >= 9:
			l7 = l7-l7
			q4 = x*4
			paths.append(3)
		else:
			l7 = 1-l7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		x = l7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))