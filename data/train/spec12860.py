import numpy as np 

def function(x):

	s5 = 9
	c3 = x
	paths = []
	try:
		if s5 >= 5:
			s5 = s5-5
			paths.append(1)
		else:
			c3 = c3-6
			c3 = c3/8
			x = x*x
			paths.append(2)
		if s5 <= 3:
			x = c3*6
			paths.append(3)
		else:
			c3 = 5/c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))