import numpy as np 

def function(x):

	c2 = 8
	u5 = x
	paths = []
	try:
		if x <= 8:
			x = x/6
			c2 = c2+u5
			c2 = 4/c2
			paths.append(1)
		else:
			c2 = u5/c2
			u5 = 4-u5
			u5 = x*x
			paths.append(2)
		if c2 > 3:
			u5 = u5/5
			c2 = 4-x
			paths.append(3)
		else:
			u5 = 9/u5
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))