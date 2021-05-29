import numpy as np 

def function(x):

	p5 = x
	s7 = 0
	paths = []
	try:
		if s7 < 5:
			x = 0*x
			x = x*s7
			x = 1+x
			paths.append(1)
		else:
			p5 = s7+7
			paths.append(2)
		if x >= 5:
			x = x-x
			s7 = 0/s7
			paths.append(3)
		else:
			x = s7-x
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