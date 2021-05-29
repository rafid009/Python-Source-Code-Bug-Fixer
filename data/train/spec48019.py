import numpy as np 

def function(x):

	s5 = x
	c4 = x
	paths = []
	try:
		if c4 >= 9:
			c4 = 9+x
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if s5 > 7:
			c4 = 4/c4
			paths.append(3)
		else:
			c4 = x/5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))