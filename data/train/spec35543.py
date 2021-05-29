import numpy as np 

def function(x):

	j0 = 6
	c4 = x
	paths = []
	try:
		if j0 <= 3:
			j0 = j0*2
			c4 = 2+c4
			j0 = j0*c4
			paths.append(1)
		else:
			c4 = 3*c4
			j0 = j0+5
			x = 4+x
			paths.append(2)
		if j0 <= 0:
			j0 = j0-1
			x = x*9
			j0 = c4+j0
			paths.append(3)
		else:
			j0 = j0-c4
			c4 = c4-0
			c4 = 3+x
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))