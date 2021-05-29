import numpy as np 

def function(x):

	u1 = 9
	z6 = 2
	paths = []
	try:
		if x < 2:
			x = x-1
			paths.append(1)
		else:
			x = 4-0
			paths.append(2)
		if z6 >= 5:
			x = x+7
			paths.append(3)
		else:
			z6 = z6-9
			x = 8/4
			z6 = 4/z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		u1 = z6**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))