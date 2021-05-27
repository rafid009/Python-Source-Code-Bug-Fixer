import numpy as np 

def function(x):

	l2 = 1
	s5 = x
	paths = []
	try:
		if l2 <= 8:
			s5 = s5/5
			paths.append(1)
		else:
			l2 = 2+8
			l2 = 1-1
			s5 = 8/s5
			paths.append(2)
		if s5 < 8:
			s5 = 6/s5
			paths.append(3)
		else:
			x = 0*x
			l2 = s5/l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))