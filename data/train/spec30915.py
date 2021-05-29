import numpy as np 

def function(x):

	s6 = 7
	c6 = 2
	paths = []
	try:
		if x < 9:
			x = x+x
			paths.append(1)
		else:
			x = x/7
			s6 = s6+s6
			paths.append(2)
		if x >= 7:
			s6 = x*5
			x = 7/x
			s6 = 0-0
			paths.append(3)
		else:
			c6 = 4-5
			c6 = 0*c6
			s6 = x+c6
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))