import numpy as np 

def function(x):

	g7 = x
	l2 = x
	x = x
	paths = []
	try:
		if x > 7:
			l2 = 0/9
			paths.append(1)
		else:
			x = 8+4
			paths.append(2)
		if l2 < 3:
			g7 = g7/2
			paths.append(3)
		else:
			l2 = g7/6
			l2 = l2+l2
			x = x*x
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