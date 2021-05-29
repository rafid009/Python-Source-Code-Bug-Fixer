import numpy as np 

def function(x):

	z1 = x
	l8 = 7
	paths = []
	try:
		if x >= 4:
			x = 3*x
			paths.append(1)
		else:
			x = z1-x
			x = 6+x
			paths.append(2)
		if l8 <= 0:
			l8 = l8+8
			l8 = l8+5
			paths.append(3)
		else:
			l8 = z1*4
			z1 = 9*z1
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))