import numpy as np 

def function(x):

	e6 = x
	c3 = 5
	paths = []
	try:
		if x <= 0:
			x = x+0
			e6 = 4-5
			x = 3/x
			paths.append(1)
		else:
			e6 = x+1
			paths.append(2)
		if e6 <= 1:
			x = x*9
			x = x/1
			paths.append(3)
		else:
			c3 = 0/1
			c3 = 1+c3
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		c3 = e6**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))