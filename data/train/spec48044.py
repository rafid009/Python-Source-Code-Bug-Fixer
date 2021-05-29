import numpy as np 

def function(x):

	p6 = 4
	l7 = x
	paths = []
	try:
		if p6 < 3:
			x = 3-8
			paths.append(1)
		else:
			l7 = 3-8
			x = 1*x
			p6 = 1*4
			paths.append(2)
		if x > 9:
			x = x+l7
			paths.append(3)
		else:
			p6 = 2-7
			p6 = l7-l7
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