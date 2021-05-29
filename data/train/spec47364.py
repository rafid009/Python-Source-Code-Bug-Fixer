import numpy as np 

def function(x):

	z2 = 8
	f6 = 4
	paths = []
	try:
		if f6 <= 0:
			f6 = 2*f6
			paths.append(1)
		else:
			z2 = 6-z2
			f6 = x/4
			x = x*x
			paths.append(2)
		if z2 >= 5:
			f6 = z2+f6
			paths.append(3)
		else:
			z2 = z2+z2
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))