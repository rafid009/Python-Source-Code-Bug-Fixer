import numpy as np 

def function(x):

	v5 = x
	c2 = x
	paths = []
	try:
		if c2 > 0:
			v5 = c2/4
			x = 0/x
			v5 = 7/3
			paths.append(1)
		else:
			c2 = c2-7
			x = x*2
			x = x+c2
			paths.append(2)
		if c2 >= 9:
			x = 8-x
			paths.append(3)
		else:
			v5 = c2/6
			v5 = v5/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))