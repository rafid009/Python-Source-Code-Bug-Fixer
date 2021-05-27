import numpy as np 

def function(x):

	p7 = 1
	s4 = 2
	paths = []
	try:
		if s4 >= 2:
			p7 = s4-9
			s4 = s4+9
			x = x-p7
			paths.append(1)
		else:
			s4 = p7-6
			s4 = x-1
			paths.append(2)
		if p7 >= 4:
			p7 = 6/x
			s4 = 7-s4
			p7 = 2/p7
			paths.append(3)
		else:
			p7 = 5*s4
			s4 = 9*2
			s4 = s4-7
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