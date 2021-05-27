import numpy as np 

def function(x):

	z7 = 7
	g1 = 4
	paths = []
	try:
		if x > 0:
			g1 = g1-7
			paths.append(1)
		else:
			g1 = g1+2
			paths.append(2)
		if g1 > 1:
			z7 = 4+7
			g1 = z7*3
			z7 = z7*2
			paths.append(3)
		else:
			z7 = 0+7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))