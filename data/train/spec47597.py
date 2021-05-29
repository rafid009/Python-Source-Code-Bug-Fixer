import numpy as np 

def function(x):

	r6 = x
	c8 = 5
	paths = []
	try:
		if r6 < 3:
			x = x/x
			x = x+c8
			x = x+9
			paths.append(1)
		else:
			x = c8*3
			r6 = r6*x
			paths.append(2)
		if c8 < 5:
			r6 = 2-1
			paths.append(3)
		else:
			c8 = c8+0
			c8 = 6/c8
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