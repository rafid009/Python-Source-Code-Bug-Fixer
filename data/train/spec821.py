import numpy as np 

def function(x):

	e5 = 0
	c2 = 7
	x = 1
	paths = []
	try:
		if c2 < 6:
			e5 = e5-4
			x = 5/7
			paths.append(1)
		else:
			e5 = e5/4
			c2 = 5-c2
			paths.append(2)
		if c2 > 1:
			c2 = 3+c2
			paths.append(3)
		else:
			x = 6-1
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		e5 = c2**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))