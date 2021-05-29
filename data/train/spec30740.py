import numpy as np 

def function(x):

	n2 = 4
	l2 = x
	paths = []
	try:
		if n2 > 8:
			x = l2/x
			x = 2*n2
			x = 6+x
			paths.append(1)
		else:
			l2 = l2*3
			n2 = n2-n2
			paths.append(2)
		if x > 9:
			n2 = n2/8
			l2 = 1-l2
			paths.append(3)
		else:
			l2 = n2-l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))