import numpy as np 

def function(x):

	b5 = x
	c8 = x
	paths = []
	try:
		if c8 <= 2:
			c8 = 6+c8
			paths.append(1)
		else:
			c8 = c8*5
			b5 = b5+b5
			paths.append(2)
		if b5 < 0:
			x = 7+x
			b5 = b5/2
			paths.append(3)
		else:
			c8 = 2+c8
			x = x-b5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		b5 = c8**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))