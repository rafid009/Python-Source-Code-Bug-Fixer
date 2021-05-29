import numpy as np 

def function(x):

	c7 = x
	j5 = x
	paths = []
	try:
		if c7 <= 1:
			x = 5/x
			paths.append(1)
		else:
			c7 = c7*8
			c7 = 3+1
			paths.append(2)
		if j5 <= 8:
			x = 1/j5
			paths.append(3)
		else:
			j5 = j5*c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))