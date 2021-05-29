import numpy as np 

def function(x):

	g3 = x
	z9 = x
	paths = []
	try:
		if z9 > 7:
			z9 = z9-3
			paths.append(1)
		else:
			g3 = g3-7
			paths.append(2)
		if g3 >= 5:
			x = 5-x
			paths.append(3)
		else:
			x = 5-9
			g3 = g3/5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))