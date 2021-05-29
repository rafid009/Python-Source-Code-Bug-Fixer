import numpy as np 

def function(x):

	s0 = x
	l6 = x
	paths = []
	try:
		if s0 <= 8:
			x = x*l6
			s0 = s0/4
			s0 = 6-s0
			paths.append(1)
		else:
			s0 = 7*s0
			paths.append(2)
		if l6 < 6:
			s0 = s0/3
			paths.append(3)
		else:
			s0 = 6+5
			s0 = l6-x
			l6 = l6-x
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		x = s0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))