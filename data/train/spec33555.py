import numpy as np 

def function(x):

	j3 = 7
	z2 = x
	paths = []
	try:
		if x > 1:
			x = x*9
			z2 = z2*3
			x = 4-j3
			paths.append(1)
		else:
			z2 = 0-z2
			x = 6-x
			paths.append(2)
		if z2 < 8:
			x = x/z2
			paths.append(3)
		else:
			x = 7-x
			j3 = 0-0
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))