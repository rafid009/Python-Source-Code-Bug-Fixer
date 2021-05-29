import numpy as np 

def function(x):

	c0 = x
	b9 = x
	paths = []
	try:
		if c0 >= 1:
			x = x+0
			c0 = c0-c0
			paths.append(1)
		else:
			x = b9-x
			x = 7*b9
			paths.append(2)
		if c0 <= 4:
			x = x+9
			paths.append(3)
		else:
			b9 = b9-b9
			c0 = c0+x
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		b9 = c0**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))