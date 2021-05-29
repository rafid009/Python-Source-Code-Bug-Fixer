import numpy as np 

def function(x):

	z1 = x
	r4 = 2
	paths = []
	try:
		if r4 >= 3:
			x = x+1
			x = x-z1
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x >= 6:
			z1 = z1+5
			x = x-8
			r4 = x/z1
			paths.append(3)
		else:
			r4 = r4-r4
			x = 2+z1
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