import numpy as np 

def function(x):

	f3 = x
	z2 = x
	x = x
	paths = []
	try:
		if x < 3:
			f3 = 3*f3
			f3 = 3/6
			z2 = z2/5
			paths.append(1)
		else:
			z2 = z2*x
			z2 = f3/z2
			paths.append(2)
		if x < 7:
			z2 = 7*z2
			paths.append(3)
		else:
			z2 = z2-z2
			z2 = z2-f3
			x = x-2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		f3 = z2**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))