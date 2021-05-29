import numpy as np 

def function(x):

	l3 = 7
	s4 = 1
	paths = []
	try:
		if s4 < 8:
			s4 = 8+x
			s4 = s4+x
			paths.append(1)
		else:
			x = 3/s4
			s4 = s4/3
			paths.append(2)
		if l3 >= 0:
			x = 8/s4
			l3 = 7+0
			x = 7+x
			paths.append(3)
		else:
			s4 = s4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))