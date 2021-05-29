import numpy as np 

def function(x):

	z9 = x
	n9 = 1
	x = 4
	paths = []
	try:
		if n9 >= 3:
			x = x-4
			x = n9+3
			z9 = 0+z9
			paths.append(1)
		else:
			n9 = z9+3
			n9 = n9/z9
			x = x+6
			paths.append(2)
		if x < 9:
			z9 = z9-4
			paths.append(3)
		else:
			x = x+x
			n9 = 2-n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))