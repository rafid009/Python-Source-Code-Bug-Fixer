import numpy as np 

def function(x):

	r5 = x
	c8 = 0
	paths = []
	try:
		if r5 <= 1:
			c8 = c8+1
			paths.append(1)
		else:
			r5 = 8*r5
			paths.append(2)
		if r5 < 9:
			x = x+5
			c8 = 8*3
			x = 3/x
			paths.append(3)
		else:
			c8 = c8*6
			r5 = 6-r5
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