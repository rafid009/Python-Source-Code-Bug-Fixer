import numpy as np 

def function(x):

	c6 = 5
	t6 = 4
	paths = []
	try:
		if x < 5:
			c6 = t6-5
			paths.append(1)
		else:
			x = x/6
			x = 1-x
			c6 = 0-c6
			paths.append(2)
		if t6 >= 9:
			c6 = c6/c6
			t6 = 9+t6
			paths.append(3)
		else:
			x = 7/x
			x = 6/6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))