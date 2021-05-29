import numpy as np 

def function(x):

	c2 = 5
	j2 = x
	paths = []
	try:
		if c2 < 8:
			j2 = 0/9
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if x <= 8:
			j2 = 2-7
			x = x/5
			c2 = c2-9
			paths.append(3)
		else:
			j2 = j2-6
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