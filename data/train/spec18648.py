import numpy as np 

def function(x):

	z9 = 8
	f6 = 3
	paths = []
	try:
		if z9 > 5:
			z9 = z9-7
			z9 = 7/z9
			paths.append(1)
		else:
			f6 = x*1
			x = z9*f6
			f6 = x*z9
			paths.append(2)
		if x <= 6:
			z9 = 1/2
			paths.append(3)
		else:
			f6 = f6-z9
			f6 = f6-x
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		z9 = f6**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))