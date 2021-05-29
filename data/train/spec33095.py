import numpy as np 

def function(x):

	f6 = 8
	c2 = x
	paths = []
	try:
		if x < 8:
			c2 = 9/3
			c2 = x+x
			c2 = c2+3
			paths.append(1)
		else:
			c2 = c2/2
			x = f6+x
			c2 = 4-9
			paths.append(2)
		if f6 <= 8:
			x = x/5
			f6 = f6+x
			paths.append(3)
		else:
			c2 = f6+c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))