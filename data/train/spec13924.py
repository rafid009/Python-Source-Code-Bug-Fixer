import numpy as np 

def function(x):

	c4 = 6
	s1 = x
	x = 7
	paths = []
	try:
		if s1 <= 3:
			s1 = s1+x
			c4 = 5-c4
			paths.append(1)
		else:
			c4 = c4-5
			s1 = x/9
			c4 = c4*c4
			paths.append(2)
		if x <= 9:
			x = x+c4
			x = x-1
			s1 = x+2
			paths.append(3)
		else:
			c4 = 1*c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))