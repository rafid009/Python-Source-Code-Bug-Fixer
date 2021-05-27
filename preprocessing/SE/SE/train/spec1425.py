import numpy as np 

def function(x):

	c1 = 7
	l3 = 7
	paths = []
	try:
		if l3 <= 4:
			x = x/3
			l3 = 8-l3
			c1 = c1/6
			paths.append(1)
		else:
			c1 = x-c1
			l3 = l3-l3
			l3 = 9+l3
			paths.append(2)
		if c1 >= 4:
			l3 = 9-l3
			l3 = 7*x
			l3 = 4/9
			paths.append(3)
		else:
			l3 = 8/8
			x = x/5
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))