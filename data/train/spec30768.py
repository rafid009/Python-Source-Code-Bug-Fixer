import numpy as np 

def function(x):

	c5 = 2
	e5 = x
	paths = []
	try:
		if e5 <= 3:
			c5 = c5*9
			paths.append(1)
		else:
			c5 = c5*6
			c5 = x+2
			paths.append(2)
		if c5 > 3:
			c5 = e5/c5
			x = c5+1
			x = x/x
			paths.append(3)
		else:
			x = x*1
			x = 5+3
			c5 = 5*c5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))