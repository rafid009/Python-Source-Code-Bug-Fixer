import numpy as np 

def function(x):

	b1 = 1
	c5 = x
	paths = []
	try:
		if c5 < 2:
			c5 = x+c5
			paths.append(1)
		else:
			c5 = c5/8
			paths.append(2)
		if b1 <= 0:
			x = c5-4
			x = 1+x
			c5 = c5/5
			paths.append(3)
		else:
			b1 = 3/b1
			b1 = 5-x
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))