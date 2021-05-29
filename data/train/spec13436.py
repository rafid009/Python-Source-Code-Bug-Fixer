import numpy as np 

def function(x):

	c3 = 5
	v4 = x
	paths = []
	try:
		if c3 < 1:
			c3 = 3-v4
			paths.append(1)
		else:
			v4 = 0/9
			v4 = 9*v4
			v4 = 7-v4
			paths.append(2)
		if v4 <= 5:
			x = x*x
			c3 = v4-5
			x = 1-x
			paths.append(3)
		else:
			c3 = 7-v4
			c3 = v4/3
			v4 = v4*x
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))