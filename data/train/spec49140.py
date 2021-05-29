import numpy as np 

def function(x):

	c1 = x
	i1 = 6
	paths = []
	try:
		if c1 >= 9:
			i1 = i1/c1
			paths.append(1)
		else:
			x = 5/9
			paths.append(2)
		if c1 < 6:
			c1 = x-9
			x = 0-c1
			x = 6/i1
			paths.append(3)
		else:
			i1 = i1*x
			i1 = i1/7
			c1 = x+c1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		i1 = c1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))