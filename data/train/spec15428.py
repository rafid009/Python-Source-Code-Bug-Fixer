import numpy as np 

def function(x):

	c3 = 5
	u3 = x
	paths = []
	try:
		if c3 <= 2:
			x = 1/x
			x = u3-u3
			paths.append(1)
		else:
			x = 1*6
			c3 = 4-c3
			c3 = 3*c3
			paths.append(2)
		if u3 <= 1:
			c3 = u3-c3
			c3 = c3/7
			c3 = 6/c3
			paths.append(3)
		else:
			u3 = 2+u3
			u3 = c3-7
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))