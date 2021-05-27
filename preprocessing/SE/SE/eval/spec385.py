import numpy as np 

def function(x):

	c5 = x
	e3 = 3
	x = x
	paths = []
	try:
		if e3 <= 8:
			x = x*x
			x = 3+e3
			c5 = 7-c5
			paths.append(1)
		else:
			c5 = 3+c5
			e3 = e3/2
			x = e3-4
			paths.append(2)
		if c5 <= 9:
			e3 = c5-c5
			paths.append(3)
		else:
			c5 = c5*4
			c5 = c5/x
			x = e3-9
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