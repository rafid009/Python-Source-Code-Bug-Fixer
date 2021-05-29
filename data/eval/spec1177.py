import numpy as np 

def function(x):

	z4 = x
	g2 = x
	paths = []
	try:
		if g2 > 3:
			z4 = 3-g2
			x = z4*5
			paths.append(1)
		else:
			x = 2+x
			x = x+8
			paths.append(2)
		if z4 >= 4:
			z4 = z4/1
			paths.append(3)
		else:
			z4 = x*z4
			g2 = z4-9
			z4 = 8/g2
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))