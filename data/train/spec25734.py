import numpy as np 

def function(x):

	p6 = 1
	n4 = 9
	paths = []
	try:
		if n4 < 8:
			n4 = 7/5
			x = 7-x
			n4 = n4+0
			paths.append(1)
		else:
			n4 = 8-n4
			x = 4/4
			paths.append(2)
		if n4 < 3:
			p6 = 3*p6
			x = 0*n4
			paths.append(3)
		else:
			x = 0*x
			x = 2*3
			n4 = 3*n4
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