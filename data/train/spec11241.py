import numpy as np 

def function(x):

	c9 = x
	r0 = x
	paths = []
	try:
		if c9 < 3:
			x = x+0
			r0 = r0*1
			paths.append(1)
		else:
			c9 = 4+7
			paths.append(2)
		if x >= 9:
			x = 9+x
			r0 = r0-3
			paths.append(3)
		else:
			r0 = r0-c9
			c9 = c9+9
			c9 = 2+2
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))