import numpy as np 

def function(x):

	b2 = 6
	c7 = 5
	paths = []
	try:
		if b2 >= 6:
			c7 = c7/9
			b2 = b2-b2
			paths.append(1)
		else:
			b2 = x/b2
			c7 = 7*3
			b2 = 7*8
			paths.append(2)
		if b2 >= 5:
			x = x/1
			c7 = 8-8
			paths.append(3)
		else:
			x = x+3
			c7 = 2+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))