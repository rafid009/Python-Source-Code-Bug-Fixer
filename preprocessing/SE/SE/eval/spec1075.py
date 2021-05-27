import numpy as np 

def function(x):

	c4 = x
	v0 = x
	x = x
	paths = []
	try:
		if x > 0:
			c4 = c4-4
			v0 = v0+6
			x = c4+2
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if v0 < 3:
			x = 7*x
			c4 = c4+0
			c4 = c4/6
			paths.append(3)
		else:
			v0 = v0-5
			v0 = v0-5
			x = 2*c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		v0 = c4**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))