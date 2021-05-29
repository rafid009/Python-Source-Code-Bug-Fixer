import numpy as np 

def function(x):

	g5 = 0
	z2 = x
	paths = []
	try:
		if g5 >= 7:
			x = 6-8
			z2 = z2/x
			g5 = 0/2
			paths.append(1)
		else:
			x = x*z2
			paths.append(2)
		if x < 6:
			g5 = 6+4
			paths.append(3)
		else:
			x = x+9
			x = g5*5
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))