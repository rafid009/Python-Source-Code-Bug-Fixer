import numpy as np 

def function(x):

	z1 = 5
	n3 = 9
	paths = []
	try:
		if z1 > 3:
			n3 = n3*x
			z1 = n3+z1
			n3 = 0*8
			paths.append(1)
		else:
			n3 = n3-8
			paths.append(2)
		if z1 > 9:
			x = x*8
			x = 0/z1
			n3 = n3+8
			paths.append(3)
		else:
			z1 = x+6
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))