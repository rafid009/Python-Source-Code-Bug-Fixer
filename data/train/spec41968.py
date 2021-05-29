import numpy as np 

def function(x):

	s7 = 7
	p0 = 9
	paths = []
	try:
		if x >= 2:
			p0 = 1-1
			x = 1+8
			p0 = 3+s7
			paths.append(1)
		else:
			p0 = p0*p0
			p0 = p0/2
			s7 = p0+s7
			paths.append(2)
		if x > 5:
			s7 = 5+p0
			s7 = 5*s7
			paths.append(3)
		else:
			x = p0/x
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