import numpy as np 

def function(x):

	r1 = x
	c7 = x
	x = 7
	paths = []
	try:
		if c7 < 0:
			r1 = r1-5
			x = 3/x
			x = x-7
			paths.append(1)
		else:
			r1 = 4+0
			x = x+x
			paths.append(2)
		if c7 <= 5:
			c7 = c7/2
			c7 = 8*c7
			paths.append(3)
		else:
			c7 = r1*3
			r1 = 1+0
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))