import numpy as np 

def function(x):

	v0 = x
	c4 = 9
	x = 8
	paths = []
	try:
		if c4 > 0:
			v0 = x-v0
			v0 = v0-7
			paths.append(1)
		else:
			v0 = v0-5
			c4 = c4*x
			paths.append(2)
		if c4 < 8:
			x = v0-x
			x = x/6
			paths.append(3)
		else:
			v0 = x+v0
			c4 = v0+c4
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))