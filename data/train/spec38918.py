import numpy as np 

def function(x):

	z4 = x
	f2 = 8
	paths = []
	try:
		if z4 < 8:
			f2 = f2*z4
			z4 = 9+0
			paths.append(1)
		else:
			f2 = 9+f2
			paths.append(2)
		if z4 < 9:
			f2 = f2+f2
			f2 = 9*f2
			z4 = z4-f2
			paths.append(3)
		else:
			f2 = f2-8
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		z4 = f2**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))