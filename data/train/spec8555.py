import numpy as np 

def function(x):

	q7 = x
	l7 = 7
	paths = []
	try:
		if q7 < 0:
			l7 = l7*7
			q7 = x+6
			q7 = q7*l7
			paths.append(1)
		else:
			l7 = l7*3
			x = l7*x
			x = x-0
			paths.append(2)
		if x > 3:
			x = x+4
			q7 = q7+q7
			l7 = l7*3
			paths.append(3)
		else:
			q7 = l7-q7
			x = l7*x
			l7 = 6*l7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))