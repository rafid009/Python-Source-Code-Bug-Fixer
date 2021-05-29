import numpy as np 

def function(x):

	a7 = 4
	z1 = 6
	paths = []
	try:
		if z1 <= 3:
			a7 = a7/8
			x = z1-5
			a7 = a7+0
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if x <= 5:
			z1 = 9-z1
			a7 = x/a7
			a7 = a7+1
			paths.append(3)
		else:
			a7 = a7/1
			x = x-9
			z1 = a7+z1
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))