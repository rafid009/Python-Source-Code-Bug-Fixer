import numpy as np 

def function(x):

	b2 = 1
	c8 = 5
	paths = []
	try:
		if b2 >= 7:
			c8 = c8+5
			paths.append(1)
		else:
			b2 = 6+b2
			b2 = b2+5
			paths.append(2)
		if x <= 6:
			x = 2/x
			c8 = 2*c8
			paths.append(3)
		else:
			c8 = c8-3
			b2 = b2-5
			x = 5+c8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))