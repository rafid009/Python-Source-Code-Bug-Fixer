import numpy as np 

def function(x):

	b3 = x
	c4 = 1
	paths = []
	try:
		if x <= 9:
			b3 = b3+5
			b3 = b3+c4
			paths.append(1)
		else:
			b3 = x*4
			c4 = 4+6
			x = x*9
			paths.append(2)
		if c4 < 5:
			b3 = b3/c4
			c4 = c4*8
			paths.append(3)
		else:
			b3 = x*b3
			b3 = c4+c4
			b3 = 1/b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))