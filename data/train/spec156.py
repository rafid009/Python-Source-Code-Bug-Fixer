import numpy as np 

def function(x):

	s2 = x
	c0 = x
	paths = []
	try:
		if x >= 6:
			c0 = c0*s2
			s2 = s2*2
			paths.append(1)
		else:
			x = 6+c0
			paths.append(2)
		if s2 > 7:
			x = s2*x
			c0 = s2+c0
			paths.append(3)
		else:
			x = x+c0
			x = x*1
			x = c0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))