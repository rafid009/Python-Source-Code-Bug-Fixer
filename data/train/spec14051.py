import numpy as np 

def function(x):

	r6 = 5
	c8 = x
	paths = []
	try:
		if c8 > 1:
			x = 9/5
			r6 = r6-9
			paths.append(1)
		else:
			c8 = c8*r6
			r6 = r6*r6
			paths.append(2)
		if r6 < 6:
			x = x+4
			paths.append(3)
		else:
			c8 = x-5
			r6 = r6-6
			r6 = 8+r6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))