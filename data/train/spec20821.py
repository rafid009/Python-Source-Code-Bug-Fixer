import numpy as np 

def function(x):

	n4 = x
	l7 = 7
	paths = []
	try:
		if x < 8:
			n4 = n4+9
			paths.append(1)
		else:
			l7 = l7/3
			n4 = n4/x
			paths.append(2)
		if n4 > 7:
			l7 = l7+l7
			n4 = 9-n4
			n4 = 1+n4
			paths.append(3)
		else:
			l7 = l7-n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))