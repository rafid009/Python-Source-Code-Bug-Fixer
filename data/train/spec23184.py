import numpy as np 

def function(x):

	b6 = x
	z1 = x
	paths = []
	try:
		if x > 3:
			b6 = b6-5
			b6 = 2+z1
			paths.append(1)
		else:
			z1 = 2+z1
			paths.append(2)
		if x < 2:
			b6 = b6*4
			paths.append(3)
		else:
			z1 = z1*z1
			x = 5/z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		b6 = z1**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))