import numpy as np 

def function(x):

	b5 = 2
	c0 = x
	paths = []
	try:
		if c0 >= 1:
			x = x*b5
			x = x*c0
			x = c0*0
			paths.append(1)
		else:
			b5 = b5-c0
			paths.append(2)
		if b5 > 0:
			x = x-5
			c0 = 2-1
			paths.append(3)
		else:
			b5 = b5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))