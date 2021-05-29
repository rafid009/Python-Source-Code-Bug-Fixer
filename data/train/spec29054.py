import numpy as np 

def function(x):

	u2 = 9
	c7 = x
	x = x
	paths = []
	try:
		if x < 0:
			u2 = 4+u2
			x = x/7
			u2 = 9+1
			paths.append(1)
		else:
			x = 4+0
			x = 8+9
			paths.append(2)
		if u2 < 4:
			c7 = 8+x
			c7 = c7*2
			c7 = c7/2
			paths.append(3)
		else:
			u2 = u2-c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))