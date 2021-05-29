import numpy as np 

def function(x):

	n9 = 6
	z4 = x
	paths = []
	try:
		if x > 3:
			z4 = 9-z4
			paths.append(1)
		else:
			n9 = n9+8
			x = 5+x
			paths.append(2)
		if z4 <= 9:
			x = 2+x
			n9 = n9-x
			paths.append(3)
		else:
			n9 = x+n9
			x = x*5
			x = x+x
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