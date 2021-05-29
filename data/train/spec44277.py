import numpy as np 

def function(x):

	c2 = x
	z1 = x
	paths = []
	try:
		if c2 <= 5:
			x = x-c2
			c2 = c2+0
			c2 = c2+x
			paths.append(1)
		else:
			c2 = c2/4
			z1 = z1+c2
			z1 = c2-z1
			paths.append(2)
		if z1 < 9:
			z1 = c2/z1
			x = 7*4
			paths.append(3)
		else:
			x = x*1
			c2 = x+c2
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		z1 = c2**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))