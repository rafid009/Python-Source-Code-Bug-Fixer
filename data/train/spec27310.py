import numpy as np 

def function(x):

	s9 = 5
	c5 = x
	paths = []
	try:
		if x >= 3:
			s9 = 1-c5
			paths.append(1)
		else:
			s9 = s9-x
			s9 = 0*3
			c5 = c5/2
			paths.append(2)
		if s9 >= 3:
			s9 = s9/5
			s9 = 6+s9
			paths.append(3)
		else:
			c5 = c5*s9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))