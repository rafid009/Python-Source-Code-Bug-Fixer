import numpy as np 

def function(x):

	c7 = 5
	b3 = 0
	paths = []
	try:
		if c7 > 8:
			x = x-x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if b3 > 7:
			x = x*1
			b3 = b3*5
			paths.append(3)
		else:
			b3 = b3-x
			x = c7-b3
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))