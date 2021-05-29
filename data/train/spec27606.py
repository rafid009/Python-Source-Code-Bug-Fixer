import numpy as np 

def function(x):

	s4 = 6
	c9 = x
	paths = []
	try:
		if s4 < 5:
			x = x/6
			paths.append(1)
		else:
			c9 = x+5
			s4 = s4/x
			paths.append(2)
		if c9 >= 0:
			s4 = 5+s4
			s4 = s4/x
			s4 = s4/x
			paths.append(3)
		else:
			s4 = s4*3
			s4 = x+7
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))