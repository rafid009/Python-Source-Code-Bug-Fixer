import numpy as np 

def function(x):

	w4 = x
	z1 = x
	paths = []
	try:
		if z1 < 5:
			z1 = z1+7
			z1 = 7*z1
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if z1 >= 4:
			z1 = z1/5
			z1 = 0*z1
			x = 8-9
			paths.append(3)
		else:
			z1 = 8*z1
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		w4 = z1**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))