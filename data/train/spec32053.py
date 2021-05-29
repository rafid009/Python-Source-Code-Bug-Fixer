import numpy as np 

def function(x):

	z8 = 9
	f0 = x
	paths = []
	try:
		if f0 > 5:
			x = 8*x
			paths.append(1)
		else:
			f0 = 8+x
			f0 = 5+f0
			paths.append(2)
		if x < 0:
			z8 = f0/5
			x = 1+x
			f0 = f0/x
			paths.append(3)
		else:
			z8 = z8/9
			f0 = f0/5
			z8 = 2+f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		z8 = f0**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))