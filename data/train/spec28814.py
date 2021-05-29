import numpy as np 

def function(x):

	c8 = x
	s7 = x
	paths = []
	try:
		if c8 >= 9:
			s7 = 1-s7
			s7 = s7/6
			paths.append(1)
		else:
			x = x-7
			s7 = s7+c8
			paths.append(2)
		if c8 < 6:
			s7 = s7/7
			paths.append(3)
		else:
			c8 = 0+0
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))