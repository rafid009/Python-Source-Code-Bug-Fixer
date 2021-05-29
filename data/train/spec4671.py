import numpy as np 

def function(x):

	g9 = 3
	z7 = 7
	paths = []
	try:
		if g9 < 8:
			z7 = 4/z7
			x = 2*x
			x = g9+6
			paths.append(1)
		else:
			z7 = z7+9
			z7 = 4/3
			x = 9+3
			paths.append(2)
		if z7 <= 9:
			g9 = g9-5
			paths.append(3)
		else:
			g9 = x-9
			z7 = x*z7
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		z7 = g9**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))