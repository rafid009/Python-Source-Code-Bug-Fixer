import numpy as np 

def function(x):

	p1 = x
	c3 = 9
	x = 7
	paths = []
	try:
		if x > 8:
			x = x/c3
			p1 = x/p1
			paths.append(1)
		else:
			c3 = 8/2
			c3 = 6*c3
			paths.append(2)
		if c3 <= 7:
			c3 = 1*c3
			paths.append(3)
		else:
			x = 9+x
			c3 = p1+c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))