import numpy as np 

def function(x):

	p6 = x
	s7 = 8
	paths = []
	try:
		if p6 > 3:
			x = x+5
			s7 = s7-x
			paths.append(1)
		else:
			p6 = p6/8
			p6 = p6-8
			s7 = s7-5
			paths.append(2)
		if s7 > 0:
			p6 = 6*8
			paths.append(3)
		else:
			s7 = 3*s7
			x = x/x
			s7 = 1+s7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))