import numpy as np 

def function(x):

	c7 = x
	r5 = x
	paths = []
	try:
		if r5 > 5:
			x = 8/x
			x = x-9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if r5 <= 3:
			c7 = c7/4
			c7 = 6/4
			paths.append(3)
		else:
			c7 = c7/9
			r5 = r5*0
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		c7 = r5**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))