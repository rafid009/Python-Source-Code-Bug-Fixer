import numpy as np 

def function(x):

	s4 = x
	l7 = x
	x = x
	paths = []
	try:
		if s4 <= 7:
			s4 = s4-x
			x = 6*x
			x = x*1
			paths.append(1)
		else:
			s4 = s4+x
			s4 = s4*7
			paths.append(2)
		if s4 < 0:
			l7 = l7*8
			s4 = s4*7
			s4 = l7+s4
			paths.append(3)
		else:
			s4 = s4-3
			l7 = x*4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))