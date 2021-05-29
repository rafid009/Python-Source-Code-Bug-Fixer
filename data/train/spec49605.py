import numpy as np 

def function(x):

	s0 = 2
	l3 = 4
	paths = []
	try:
		if x < 7:
			s0 = 4+0
			paths.append(1)
		else:
			l3 = l3-l3
			x = 7-4
			s0 = 7+s0
			paths.append(2)
		if s0 <= 0:
			l3 = l3+6
			x = x-7
			paths.append(3)
		else:
			s0 = s0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))