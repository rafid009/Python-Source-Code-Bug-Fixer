import numpy as np 

def function(x):

	l8 = x
	n4 = 5
	paths = []
	try:
		if l8 <= 0:
			x = 6-3
			x = 6+5
			paths.append(1)
		else:
			n4 = 9-n4
			l8 = 1+x
			l8 = 2-6
			paths.append(2)
		if n4 > 0:
			l8 = l8*n4
			l8 = l8+n4
			paths.append(3)
		else:
			x = x*x
			n4 = n4*l8
			n4 = n4+6
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		n4 = l8**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))