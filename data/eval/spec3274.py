import numpy as np 

def function(x):

	z1 = 6
	r8 = 2
	paths = []
	try:
		if x > 9:
			z1 = z1*2
			paths.append(1)
		else:
			x = x-1
			x = x*6
			paths.append(2)
		if z1 > 8:
			z1 = 5-z1
			paths.append(3)
		else:
			z1 = z1-z1
			x = 2/6
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		r8 = z1**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))