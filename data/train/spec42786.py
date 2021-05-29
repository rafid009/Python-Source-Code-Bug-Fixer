import numpy as np 

def function(x):

	n3 = 8
	l2 = x
	paths = []
	try:
		if n3 < 3:
			x = x/2
			l2 = x*1
			paths.append(1)
		else:
			n3 = 4*n3
			paths.append(2)
		if x <= 7:
			n3 = x*x
			n3 = 7-n3
			l2 = 5-l2
			paths.append(3)
		else:
			x = 9-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))