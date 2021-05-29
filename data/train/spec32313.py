import numpy as np 

def function(x):

	i0 = 7
	c5 = x
	paths = []
	try:
		if i0 < 1:
			c5 = 1/c5
			x = x*4
			c5 = c5+2
			paths.append(1)
		else:
			c5 = i0+1
			paths.append(2)
		if c5 > 1:
			i0 = i0+x
			paths.append(3)
		else:
			c5 = c5*0
			c5 = 3/c5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))