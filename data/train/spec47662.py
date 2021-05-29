import numpy as np 

def function(x):

	c3 = 5
	u9 = x
	x = x
	paths = []
	try:
		if c3 > 7:
			c3 = 5/c3
			paths.append(1)
		else:
			c3 = u9-c3
			u9 = u9/x
			paths.append(2)
		if c3 >= 4:
			c3 = c3-u9
			paths.append(3)
		else:
			c3 = 8+c3
			u9 = 6*c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		u9 = c3**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))