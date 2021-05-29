import numpy as np 

def function(x):

	p8 = x
	s4 = x
	paths = []
	try:
		if p8 >= 3:
			p8 = 6*p8
			s4 = 8+s4
			p8 = x/x
			paths.append(1)
		else:
			s4 = s4-9
			s4 = s4-6
			paths.append(2)
		if s4 >= 9:
			p8 = p8*s4
			x = 5+6
			x = s4/x
			paths.append(3)
		else:
			s4 = 9*x
			s4 = 2/s4
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