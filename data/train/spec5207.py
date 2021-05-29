import numpy as np 

def function(x):

	s5 = 9
	p6 = 4
	paths = []
	try:
		if x >= 6:
			s5 = 0*s5
			p6 = s5-3
			paths.append(1)
		else:
			s5 = s5/4
			p6 = 9/x
			s5 = 6*p6
			paths.append(2)
		if s5 < 6:
			x = 7/x
			paths.append(3)
		else:
			x = p6-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))