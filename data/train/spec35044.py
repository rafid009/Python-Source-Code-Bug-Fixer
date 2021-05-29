import numpy as np 

def function(x):

	q7 = x
	l6 = 6
	paths = []
	try:
		if x >= 1:
			q7 = q7*2
			q7 = 4/q7
			l6 = 6-l6
			paths.append(1)
		else:
			q7 = 2+q7
			paths.append(2)
		if q7 > 4:
			l6 = l6+2
			x = x/2
			paths.append(3)
		else:
			l6 = 4+6
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