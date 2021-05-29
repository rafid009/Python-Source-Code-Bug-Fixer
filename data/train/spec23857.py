import numpy as np 

def function(x):

	f7 = 8
	z1 = 3
	paths = []
	try:
		if x <= 6:
			z1 = z1-x
			z1 = x/4
			z1 = z1*z1
			paths.append(1)
		else:
			z1 = f7*5
			x = x*x
			paths.append(2)
		if z1 <= 5:
			f7 = x*1
			f7 = 5/f7
			f7 = f7+f7
			paths.append(3)
		else:
			f7 = 9-x
			z1 = z1*f7
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