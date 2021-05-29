import numpy as np 

def function(x):

	l7 = x
	s0 = 8
	paths = []
	try:
		if l7 > 1:
			l7 = l7-6
			x = 1-3
			l7 = l7/5
			paths.append(1)
		else:
			s0 = 1-s0
			s0 = 8/2
			x = 7+l7
			paths.append(2)
		if x >= 6:
			l7 = l7/1
			x = 8+2
			x = 7-x
			paths.append(3)
		else:
			x = x+0
			x = 0*x
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