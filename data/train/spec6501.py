import numpy as np 

def function(x):

	s7 = x
	c1 = 4
	paths = []
	try:
		if c1 <= 1:
			c1 = s7/9
			c1 = c1+1
			x = 1*x
			paths.append(1)
		else:
			x = 7*x
			x = x+s7
			s7 = s7-6
			paths.append(2)
		if s7 <= 5:
			x = x+0
			paths.append(3)
		else:
			c1 = 4/s7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))