import numpy as np 

def function(x):

	l2 = 8
	x6 = x
	paths = []
	try:
		if l2 < 1:
			l2 = 0/l2
			x = 3-x6
			x = 3+6
			paths.append(1)
		else:
			l2 = 1-l2
			x6 = 1-x6
			l2 = 0-l2
			paths.append(2)
		if x >= 9:
			x6 = 0+9
			l2 = x*9
			paths.append(3)
		else:
			x6 = 0-4
			l2 = l2/x6
			x6 = 2-3
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x6 = l2**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))