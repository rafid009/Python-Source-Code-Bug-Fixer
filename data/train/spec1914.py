import numpy as np 

def function(x):

	c6 = x
	z9 = x
	paths = []
	try:
		if z9 < 8:
			c6 = c6+7
			z9 = z9-9
			paths.append(1)
		else:
			z9 = z9/2
			z9 = z9*c6
			paths.append(2)
		if x > 4:
			c6 = z9/5
			x = x*1
			paths.append(3)
		else:
			x = x+x
			x = c6/c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))