import numpy as np 

def function(x):

	c3 = 2
	r5 = x
	paths = []
	try:
		if r5 <= 4:
			c3 = c3/r5
			r5 = x*r5
			r5 = c3*r5
			paths.append(1)
		else:
			r5 = 7*r5
			r5 = 7/r5
			paths.append(2)
		if c3 > 6:
			r5 = r5/1
			c3 = 3+c3
			paths.append(3)
		else:
			x = 6/x
			c3 = x-8
			r5 = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))