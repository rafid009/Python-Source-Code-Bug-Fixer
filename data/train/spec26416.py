import numpy as np 

def function(x):

	n3 = x
	z1 = x
	paths = []
	try:
		if z1 <= 5:
			x = x+n3
			paths.append(1)
		else:
			z1 = z1*9
			paths.append(2)
		if z1 < 4:
			n3 = z1*n3
			paths.append(3)
		else:
			x = z1-x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		n3 = z1**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))