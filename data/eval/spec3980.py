import numpy as np 

def function(x):

	l0 = x
	s2 = 4
	paths = []
	try:
		if l0 >= 5:
			l0 = l0+9
			l0 = l0-2
			s2 = s2+1
			paths.append(1)
		else:
			x = 9-1
			s2 = s2-5
			x = 8-x
			paths.append(2)
		if s2 > 6:
			l0 = l0+8
			x = 2+x
			s2 = x-l0
			paths.append(3)
		else:
			x = 7*6
			x = 7*s2
			l0 = l0-4
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		s2 = l0**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))