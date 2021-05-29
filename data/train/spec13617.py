import numpy as np 

def function(x):

	c4 = x
	k2 = 4
	paths = []
	try:
		if c4 > 3:
			x = x-9
			c4 = c4*x
			paths.append(1)
		else:
			k2 = k2+x
			x = x*7
			paths.append(2)
		if c4 <= 7:
			c4 = 5-1
			x = c4+4
			paths.append(3)
		else:
			c4 = 8*0
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))