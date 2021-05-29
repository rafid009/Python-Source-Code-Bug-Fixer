import numpy as np 

def function(x):

	c1 = 6
	s6 = x
	paths = []
	try:
		if s6 >= 1:
			c1 = 6*c1
			x = x/1
			s6 = 6-s6
			paths.append(1)
		else:
			c1 = 0-9
			paths.append(2)
		if x > 0:
			c1 = x/7
			c1 = s6-4
			c1 = c1*7
			paths.append(3)
		else:
			s6 = s6/s6
			s6 = 8/6
			x = 2*6
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))