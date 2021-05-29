import numpy as np 

def function(x):

	c7 = 9
	t7 = x
	paths = []
	try:
		if x > 5:
			c7 = c7*c7
			x = x-x
			paths.append(1)
		else:
			c7 = c7*3
			c7 = 4/t7
			paths.append(2)
		if x >= 9:
			c7 = 5/c7
			t7 = t7*9
			paths.append(3)
		else:
			x = x*c7
			x = 7*7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))