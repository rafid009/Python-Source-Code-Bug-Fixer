import numpy as np 

def function(x):

	c5 = x
	g9 = 0
	paths = []
	try:
		if x > 5:
			c5 = x*c5
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x >= 6:
			x = x-2
			paths.append(3)
		else:
			x = c5+x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))