import numpy as np 

def function(x):

	z4 = x
	x9 = 8
	paths = []
	try:
		if x9 <= 3:
			x9 = z4+0
			paths.append(1)
		else:
			x9 = x9-z4
			z4 = z4*9
			z4 = x9*4
			paths.append(2)
		if x9 < 5:
			x = x+x
			x = x/8
			paths.append(3)
		else:
			x9 = 5/x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))