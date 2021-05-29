import numpy as np 

def function(x):

	r2 = x
	c1 = x
	paths = []
	try:
		if x > 5:
			x = r2/9
			r2 = r2/r2
			paths.append(1)
		else:
			r2 = r2+r2
			paths.append(2)
		if x < 3:
			c1 = x*c1
			c1 = 3/7
			r2 = 6/c1
			paths.append(3)
		else:
			c1 = c1-6
			r2 = r2-7
			r2 = r2/x
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