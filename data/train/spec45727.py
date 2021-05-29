import numpy as np 

def function(x):

	p8 = 7
	l2 = x
	paths = []
	try:
		if x >= 8:
			x = 1-x
			l2 = 8/x
			paths.append(1)
		else:
			x = x*p8
			l2 = 9+l2
			p8 = p8-x
			paths.append(2)
		if l2 <= 0:
			p8 = p8+p8
			x = 6-7
			x = 9/x
			paths.append(3)
		else:
			l2 = 6-l2
			p8 = 2-p8
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))