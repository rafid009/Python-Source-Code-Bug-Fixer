import numpy as np 

def function(x):

	s6 = 4
	c2 = x
	paths = []
	try:
		if c2 < 8:
			c2 = c2*c2
			c2 = x/c2
			s6 = s6-9
			paths.append(1)
		else:
			s6 = s6+c2
			x = 0+s6
			paths.append(2)
		if c2 > 5:
			s6 = s6-8
			x = 1*1
			paths.append(3)
		else:
			x = 3+x
			s6 = x+2
			x = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s6 = x**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))