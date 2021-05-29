import numpy as np 

def function(x):

	l7 = x
	x1 = 8
	paths = []
	try:
		if x > 6:
			x = x1-x
			x1 = x1/4
			l7 = 6/5
			paths.append(1)
		else:
			x = 6*x
			x1 = x1+2
			x = x+l7
			paths.append(2)
		if x1 > 6:
			x1 = x1-7
			paths.append(3)
		else:
			x1 = x1+1
			x1 = 4*x1
			l7 = x/x1
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))