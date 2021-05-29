import numpy as np 

def function(x):

	c6 = 4
	u3 = x
	paths = []
	try:
		if c6 < 8:
			x = 8*4
			paths.append(1)
		else:
			c6 = c6-1
			paths.append(2)
		if x >= 9:
			c6 = c6+5
			paths.append(3)
		else:
			u3 = 0+c6
			c6 = 7-c6
			u3 = 0+1
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