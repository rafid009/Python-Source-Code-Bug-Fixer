import numpy as np 

def function(x):

	c5 = 9
	b5 = 2
	paths = []
	try:
		if x >= 5:
			c5 = c5+3
			x = c5+x
			paths.append(1)
		else:
			x = 5*x
			b5 = 0+b5
			paths.append(2)
		if x <= 9:
			x = x*b5
			paths.append(3)
		else:
			b5 = x+b5
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