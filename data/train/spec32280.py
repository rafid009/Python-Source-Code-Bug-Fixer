import numpy as np 

def function(x):

	l2 = 6
	x2 = 3
	paths = []
	try:
		if x2 > 7:
			l2 = l2-x
			paths.append(1)
		else:
			l2 = x/l2
			paths.append(2)
		if x2 <= 6:
			x = 4/7
			x2 = 3-x2
			paths.append(3)
		else:
			l2 = x2/l2
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