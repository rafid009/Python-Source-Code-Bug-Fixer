import numpy as np 

def function(x):

	l3 = x
	c6 = 5
	paths = []
	try:
		if c6 >= 6:
			x = x*x
			paths.append(1)
		else:
			l3 = l3/5
			l3 = l3-9
			x = 5-0
			paths.append(2)
		if l3 < 5:
			x = 7+x
			c6 = 7/4
			c6 = x*l3
			paths.append(3)
		else:
			c6 = c6-l3
			c6 = c6*0
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))