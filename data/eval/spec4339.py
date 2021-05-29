import numpy as np 

def function(x):

	s0 = 0
	l1 = 8
	paths = []
	try:
		if x > 9:
			l1 = 0*x
			x = 8*1
			paths.append(1)
		else:
			s0 = s0+s0
			paths.append(2)
		if x >= 0:
			l1 = l1-5
			l1 = 7/l1
			s0 = 1-l1
			paths.append(3)
		else:
			l1 = 9/7
			x = l1-8
			s0 = s0*7
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		s0 = l1**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))