import numpy as np 

def function(x):

	l7 = 0
	q7 = x
	paths = []
	try:
		if l7 <= 1:
			q7 = q7*x
			paths.append(1)
		else:
			l7 = 5+l7
			q7 = q7-8
			paths.append(2)
		if q7 >= 3:
			q7 = l7-q7
			x = x*6
			l7 = 8-6
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))