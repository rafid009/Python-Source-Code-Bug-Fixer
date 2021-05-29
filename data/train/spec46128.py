import numpy as np 

def function(x):

	z1 = x
	r6 = x
	paths = []
	try:
		if r6 >= 2:
			r6 = r6+5
			z1 = x/z1
			x = x-9
			paths.append(1)
		else:
			r6 = 9/3
			x = 3*r6
			paths.append(2)
		if r6 >= 8:
			z1 = 4+z1
			x = x/x
			paths.append(3)
		else:
			z1 = z1*x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))