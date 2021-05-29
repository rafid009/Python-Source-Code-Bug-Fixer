import numpy as np 

def function(x):

	n5 = 2
	l2 = 6
	paths = []
	try:
		if x > 2:
			x = l2-n5
			n5 = 7+l2
			paths.append(1)
		else:
			n5 = n5/l2
			x = l2/x
			paths.append(2)
		if l2 < 0:
			l2 = l2+x
			x = 8/3
			x = l2/2
			paths.append(3)
		else:
			n5 = l2+8
			n5 = 4+n5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))