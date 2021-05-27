import numpy as np 

def function(x):

	h2 = 0
	c7 = 2
	paths = []
	try:
		if c7 <= 2:
			h2 = h2+9
			h2 = 7+9
			c7 = h2*c7
			paths.append(1)
		else:
			c7 = 6+x
			x = 0+x
			paths.append(2)
		if x >= 7:
			c7 = 9-0
			x = x*6
			h2 = 1*h2
			paths.append(3)
		else:
			c7 = c7*0
			h2 = 2-3
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