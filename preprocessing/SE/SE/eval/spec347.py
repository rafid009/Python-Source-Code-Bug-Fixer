import numpy as np 

def function(x):

	p8 = x
	c7 = x
	paths = []
	try:
		if x < 7:
			c7 = c7+8
			x = x+2
			c7 = x-4
			paths.append(1)
		else:
			x = 5-x
			c7 = 4*3
			paths.append(2)
		if c7 <= 6:
			x = x*9
			x = 7*1
			paths.append(3)
		else:
			x = x*5
			c7 = 5/c7
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))