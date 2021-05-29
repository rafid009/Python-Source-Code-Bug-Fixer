import numpy as np 

def function(x):

	l4 = x
	n6 = 2
	x = x
	paths = []
	try:
		if n6 >= 7:
			l4 = 1/l4
			x = n6*x
			n6 = x/n6
			paths.append(1)
		else:
			l4 = n6/5
			n6 = n6+n6
			l4 = n6+x
			paths.append(2)
		if l4 > 0:
			n6 = n6/8
			x = x/8
			n6 = n6*8
			paths.append(3)
		else:
			l4 = l4+2
			n6 = 0*n6
			n6 = n6-2
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		n6 = l4**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))