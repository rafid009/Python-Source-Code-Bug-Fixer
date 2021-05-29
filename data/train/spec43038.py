import numpy as np 

def function(x):

	l4 = 1
	s0 = x
	paths = []
	try:
		if l4 >= 0:
			l4 = 1+l4
			x = x-9
			paths.append(1)
		else:
			s0 = 3/s0
			l4 = 9*5
			s0 = 5/l4
			paths.append(2)
		if x >= 2:
			l4 = 6+l4
			paths.append(3)
		else:
			s0 = 2+s0
			l4 = 5+x
			s0 = 7-s0
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))