import numpy as np 

def function(x):

	c1 = x
	j3 = x
	paths = []
	try:
		if x <= 0:
			x = 3+0
			j3 = j3/8
			j3 = 1-j3
			paths.append(1)
		else:
			j3 = j3/c1
			j3 = x/j3
			paths.append(2)
		if j3 <= 6:
			c1 = c1*9
			j3 = 8/j3
			paths.append(3)
		else:
			j3 = j3/x
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