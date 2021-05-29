import numpy as np 

def function(x):

	c2 = 5
	j6 = 3
	paths = []
	try:
		if x < 5:
			j6 = 8-9
			paths.append(1)
		else:
			c2 = c2+9
			j6 = 1*8
			j6 = j6*7
			paths.append(2)
		if c2 < 3:
			j6 = 9/9
			j6 = 7*c2
			j6 = x/j6
			paths.append(3)
		else:
			x = 8-c2
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