import numpy as np 

def function(x):

	c1 = 8
	r2 = x
	paths = []
	try:
		if r2 <= 9:
			r2 = 6+r2
			r2 = r2-6
			paths.append(1)
		else:
			r2 = r2-c1
			x = x*2
			x = x/7
			paths.append(2)
		if r2 <= 8:
			x = x+9
			x = x+r2
			paths.append(3)
		else:
			c1 = x-x
			c1 = c1-c1
			x = r2+x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		c1 = r2**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))