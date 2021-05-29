import numpy as np 

def function(x):

	l5 = 0
	q7 = 3
	paths = []
	try:
		if x > 8:
			l5 = 1-l5
			q7 = l5-q7
			x = x/6
			paths.append(1)
		else:
			q7 = 9+5
			paths.append(2)
		if q7 >= 6:
			l5 = l5*l5
			q7 = q7/x
			l5 = q7+l5
			paths.append(3)
		else:
			x = x-6
			l5 = 8/q7
			q7 = q7/7
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))