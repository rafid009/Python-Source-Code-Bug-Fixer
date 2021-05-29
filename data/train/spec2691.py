import numpy as np 

def function(x):

	i6 = 8
	c9 = x
	paths = []
	try:
		if x > 8:
			x = x+1
			paths.append(1)
		else:
			x = c9-5
			c9 = 3*x
			i6 = i6/i6
			paths.append(2)
		if x > 1:
			x = x/x
			paths.append(3)
		else:
			x = c9-x
			x = x-x
			i6 = 3*i6
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))