import numpy as np 

def function(x):

	s7 = 1
	c1 = 0
	x = 3
	paths = []
	try:
		if x >= 8:
			x = c1/5
			c1 = 5-c1
			paths.append(1)
		else:
			c1 = c1*7
			s7 = s7/6
			x = 1/x
			paths.append(2)
		if s7 <= 1:
			x = x*x
			c1 = c1-7
			s7 = s7+8
			paths.append(3)
		else:
			c1 = 6/s7
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		s7 = c1**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))