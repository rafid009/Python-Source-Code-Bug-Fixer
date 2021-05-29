import numpy as np 

def function(x):

	n4 = 2
	l1 = 1
	paths = []
	try:
		if x >= 7:
			l1 = 4/l1
			l1 = 0+l1
			l1 = l1-6
			paths.append(1)
		else:
			x = x*l1
			n4 = n4-x
			l1 = n4*l1
			paths.append(2)
		if l1 > 3:
			n4 = 4+n4
			l1 = 8-4
			n4 = 5+4
			paths.append(3)
		else:
			l1 = 5-l1
			x = x/l1
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