import numpy as np 

def function(x):

	l7 = 3
	q7 = 4
	x = 9
	paths = []
	try:
		if q7 >= 6:
			x = l7+x
			l7 = 9-1
			x = 0-x
			paths.append(1)
		else:
			x = x*7
			q7 = q7-x
			x = q7-3
			paths.append(2)
		if l7 > 1:
			l7 = 5/l7
			paths.append(3)
		else:
			x = x*5
			x = x+q7
			q7 = q7*l7
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