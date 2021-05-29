import numpy as np 

def function(x):

	s5 = x
	c2 = x
	x = x
	paths = []
	try:
		if s5 >= 3:
			x = x-7
			c2 = 1+c2
			paths.append(1)
		else:
			c2 = c2/6
			paths.append(2)
		if c2 <= 3:
			s5 = s5-4
			s5 = 4+c2
			paths.append(3)
		else:
			s5 = 3+1
			x = x-6
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		c2 = s5**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))