import numpy as np 

def function(x):

	s9 = 2
	l2 = x
	paths = []
	try:
		if l2 < 8:
			l2 = 8+l2
			s9 = s9*7
			paths.append(1)
		else:
			x = x-6
			s9 = s9/3
			s9 = 4+s9
			paths.append(2)
		if s9 >= 8:
			l2 = 0-l2
			x = x+6
			paths.append(3)
		else:
			x = 0/x
			x = x+x
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