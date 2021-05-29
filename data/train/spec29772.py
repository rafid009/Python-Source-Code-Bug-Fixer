import numpy as np 

def function(x):

	l7 = 4
	n4 = x
	paths = []
	try:
		if x <= 3:
			x = l7/8
			l7 = 8+l7
			paths.append(1)
		else:
			l7 = l7-l7
			n4 = n4-0
			l7 = 2/7
			paths.append(2)
		if n4 <= 3:
			x = n4/l7
			paths.append(3)
		else:
			x = x*l7
			n4 = n4*n4
			n4 = n4-l7
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))