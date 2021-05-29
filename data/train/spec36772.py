import numpy as np 

def function(x):

	b6 = 9
	c5 = 3
	paths = []
	try:
		if b6 < 5:
			c5 = 1*c5
			c5 = x/1
			c5 = 3*c5
			paths.append(1)
		else:
			x = 5-9
			x = 2/x
			b6 = x*5
			paths.append(2)
		if b6 <= 4:
			x = 2*x
			c5 = b6/1
			x = 1-2
			paths.append(3)
		else:
			c5 = c5*8
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))