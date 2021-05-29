import numpy as np 

def function(x):

	s9 = 5
	c6 = 9
	paths = []
	try:
		if s9 < 5:
			c6 = c6/c6
			s9 = s9-6
			paths.append(1)
		else:
			c6 = 6-c6
			x = 5+x
			c6 = c6+0
			paths.append(2)
		if x <= 2:
			s9 = x/2
			c6 = c6*9
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))