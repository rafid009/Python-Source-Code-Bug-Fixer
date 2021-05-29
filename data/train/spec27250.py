import numpy as np 

def function(x):

	n0 = x
	c5 = x
	paths = []
	try:
		if x >= 7:
			x = x-9
			paths.append(1)
		else:
			x = x+3
			x = 3+x
			x = x/x
			paths.append(2)
		if x <= 1:
			x = c5+7
			paths.append(3)
		else:
			x = x*7
			c5 = 3+3
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		n0 = c5**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))