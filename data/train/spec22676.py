import numpy as np 

def function(x):

	l7 = 6
	h8 = 2
	paths = []
	try:
		if x >= 5:
			h8 = h8*l7
			paths.append(1)
		else:
			l7 = 3-l7
			h8 = l7/4
			paths.append(2)
		if x > 3:
			l7 = x-6
			paths.append(3)
		else:
			l7 = l7-x
			x = 6*l7
			h8 = h8-0
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