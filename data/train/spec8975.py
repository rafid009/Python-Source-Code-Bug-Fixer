import numpy as np 

def function(x):

	z6 = x
	a4 = 4
	paths = []
	try:
		if z6 > 1:
			a4 = 0/a4
			a4 = a4*9
			paths.append(1)
		else:
			x = 7*8
			z6 = z6-9
			x = a4+a4
			paths.append(2)
		if x <= 7:
			a4 = x-a4
			x = 9-x
			z6 = a4/9
			paths.append(3)
		else:
			a4 = a4-x
			x = x*8
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))