import numpy as np 

def function(x):

	s5 = x
	c1 = 8
	paths = []
	try:
		if s5 < 1:
			x = x+s5
			paths.append(1)
		else:
			s5 = c1*3
			x = c1+6
			c1 = x*3
			paths.append(2)
		if x < 2:
			c1 = s5+s5
			paths.append(3)
		else:
			s5 = 3*s5
			x = x/7
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))