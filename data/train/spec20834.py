import numpy as np 

def function(x):

	j2 = 5
	c0 = 2
	paths = []
	try:
		if x >= 1:
			x = x-7
			c0 = 7+c0
			paths.append(1)
		else:
			j2 = 2-x
			j2 = 6/j2
			c0 = 6-c0
			paths.append(2)
		if x <= 3:
			x = 1+x
			j2 = j2/1
			x = x-0
			paths.append(3)
		else:
			c0 = c0*2
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