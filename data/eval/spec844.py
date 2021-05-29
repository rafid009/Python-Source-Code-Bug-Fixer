import numpy as np 

def function(x):

	c3 = x
	u1 = 5
	paths = []
	try:
		if c3 >= 8:
			u1 = x+2
			x = 6*c3
			u1 = 8-u1
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if u1 > 7:
			u1 = u1/4
			c3 = c3-1
			paths.append(3)
		else:
			c3 = 6*c3
			u1 = u1+6
			u1 = 1/3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		u1 = c3**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))