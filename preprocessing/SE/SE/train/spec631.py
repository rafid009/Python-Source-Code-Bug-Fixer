import numpy as np 

def function(x):

	c1 = x
	s9 = x
	paths = []
	try:
		if c1 >= 4:
			x = x/s9
			s9 = s9-5
			x = x*c1
			paths.append(1)
		else:
			c1 = c1+7
			c1 = 9+8
			paths.append(2)
		if x < 7:
			s9 = 3*s9
			s9 = s9+c1
			paths.append(3)
		else:
			x = 3-x
			x = x/3
			x = 5*c1
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