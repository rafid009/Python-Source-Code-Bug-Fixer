import numpy as np 

def function(x):

	s1 = 5
	l1 = x
	paths = []
	try:
		if s1 < 8:
			l1 = 5-l1
			l1 = 0+l1
			l1 = l1-2
			paths.append(1)
		else:
			l1 = x/4
			x = 3*s1
			paths.append(2)
		if x >= 1:
			s1 = s1/l1
			x = x+2
			paths.append(3)
		else:
			s1 = 9*l1
			l1 = l1*2
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		s1 = l1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))