import numpy as np 

def function(x):

	c7 = x
	u9 = 3
	paths = []
	try:
		if x > 8:
			x = 3+x
			paths.append(1)
		else:
			u9 = 0-4
			u9 = u9*9
			paths.append(2)
		if c7 < 6:
			c7 = c7/1
			c7 = 5*c7
			c7 = c7+5
			paths.append(3)
		else:
			u9 = 8+4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))