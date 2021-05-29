import numpy as np 

def function(x):

	c3 = x
	u0 = 7
	paths = []
	try:
		if x < 7:
			x = x+5
			x = c3-9
			u0 = u0/4
			paths.append(1)
		else:
			u0 = u0+8
			paths.append(2)
		if c3 >= 8:
			u0 = u0*3
			x = c3+x
			u0 = 5*6
			paths.append(3)
		else:
			u0 = 8+u0
			c3 = c3/4
			u0 = u0*u0
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		u0 = c3**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))