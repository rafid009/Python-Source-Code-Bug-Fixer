import numpy as np 

def function(x):

	l0 = x
	n4 = x
	paths = []
	try:
		if n4 < 1:
			x = x-0
			paths.append(1)
		else:
			n4 = l0+n4
			n4 = 7+1
			x = n4*n4
			paths.append(2)
		if x < 6:
			n4 = x*9
			paths.append(3)
		else:
			n4 = l0-5
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))