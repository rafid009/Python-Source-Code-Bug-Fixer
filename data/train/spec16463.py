import numpy as np 

def function(x):

	c4 = 2
	u3 = 2
	paths = []
	try:
		if c4 <= 3:
			x = x-3
			c4 = u3-7
			paths.append(1)
		else:
			u3 = u3/3
			x = 3/x
			x = c4+c4
			paths.append(2)
		if x <= 3:
			x = u3*x
			c4 = c4-4
			paths.append(3)
		else:
			x = x*x
			u3 = u3+3
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))