import numpy as np 

def function(x):

	z1 = 0
	r6 = 5
	x = x
	paths = []
	try:
		if r6 >= 8:
			z1 = x-z1
			r6 = 8+r6
			paths.append(1)
		else:
			r6 = 4+r6
			z1 = 9-z1
			r6 = r6-4
			paths.append(2)
		if r6 <= 2:
			r6 = r6*2
			r6 = r6-r6
			z1 = z1/8
			paths.append(3)
		else:
			z1 = z1*0
			z1 = r6-z1
			z1 = 8+z1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))