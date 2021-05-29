import numpy as np 

def function(x):

	o2 = 4
	l2 = 8
	paths = []
	try:
		if x <= 9:
			x = 0-x
			paths.append(1)
		else:
			x = x/2
			o2 = 9*x
			x = o2/3
			paths.append(2)
		if l2 >= 0:
			l2 = 1-l2
			paths.append(3)
		else:
			l2 = 3/7
			l2 = 8+x
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