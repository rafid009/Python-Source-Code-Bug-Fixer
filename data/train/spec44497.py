import numpy as np 

def function(x):

	z1 = 2
	u8 = x
	paths = []
	try:
		if z1 >= 3:
			x = x-u8
			z1 = 5/8
			u8 = z1/u8
			paths.append(1)
		else:
			z1 = z1-6
			paths.append(2)
		if u8 <= 8:
			z1 = z1-x
			u8 = 0/x
			z1 = z1+0
			paths.append(3)
		else:
			z1 = 3/6
			z1 = 5/3
			u8 = 3-x
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