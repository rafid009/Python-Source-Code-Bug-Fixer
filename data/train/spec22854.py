import numpy as np 

def function(x):

	c5 = x
	r5 = x
	paths = []
	try:
		if c5 <= 2:
			c5 = 0-3
			x = x*3
			c5 = c5-x
			paths.append(1)
		else:
			c5 = c5+5
			r5 = r5-9
			c5 = r5*5
			paths.append(2)
		if r5 <= 8:
			r5 = c5+r5
			x = r5/8
			x = 3*r5
			paths.append(3)
		else:
			c5 = c5/8
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))