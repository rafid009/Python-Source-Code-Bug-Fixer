import numpy as np 

def function(x):

	u3 = x
	c3 = x
	paths = []
	try:
		if x > 5:
			c3 = c3-c3
			u3 = u3*x
			x = x-4
			paths.append(1)
		else:
			x = u3+8
			u3 = 8/u3
			paths.append(2)
		if c3 <= 5:
			x = x/3
			x = x*7
			paths.append(3)
		else:
			c3 = 8+c3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))