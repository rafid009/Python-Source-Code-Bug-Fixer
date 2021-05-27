import numpy as np 

def function(x):

	n9 = x
	z6 = x
	paths = []
	try:
		if n9 <= 0:
			x = x+x
			paths.append(1)
		else:
			z6 = x/z6
			z6 = 8/5
			n9 = n9*1
			paths.append(2)
		if x <= 6:
			z6 = z6/n9
			z6 = z6-z6
			x = 6-x
			paths.append(3)
		else:
			x = 4-5
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