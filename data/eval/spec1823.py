import numpy as np 

def function(x):

	m9 = x
	l2 = 8
	paths = []
	try:
		if l2 > 4:
			l2 = 0-l2
			x = x-6
			x = x-2
			paths.append(1)
		else:
			l2 = 4*l2
			paths.append(2)
		if x <= 6:
			l2 = 8*x
			paths.append(3)
		else:
			l2 = l2*l2
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