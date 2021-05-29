import numpy as np 

def function(x):

	y8 = x
	c3 = x
	paths = []
	try:
		if x <= 2:
			x = 9*x
			x = 4*4
			c3 = c3+1
			paths.append(1)
		else:
			x = x*x
			y8 = 5-0
			paths.append(2)
		if c3 >= 9:
			c3 = x-9
			c3 = 8-c3
			c3 = c3/3
			paths.append(3)
		else:
			x = 6+x
			c3 = 2+c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))