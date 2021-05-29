import numpy as np 

def function(x):

	n6 = 7
	z1 = 8
	paths = []
	try:
		if z1 <= 0:
			z1 = 2+z1
			paths.append(1)
		else:
			x = x+n6
			x = x*2
			paths.append(2)
		if x <= 7:
			z1 = 5-z1
			x = 7/8
			paths.append(3)
		else:
			n6 = z1/5
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		n6 = z1**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))