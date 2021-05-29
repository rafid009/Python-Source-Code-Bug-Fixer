import numpy as np 

def function(x):

	f8 = 1
	z7 = 0
	paths = []
	try:
		if f8 > 5:
			f8 = f8+x
			z7 = z7+z7
			z7 = 6+z7
			paths.append(1)
		else:
			z7 = z7*9
			z7 = 9-z7
			paths.append(2)
		if f8 < 9:
			z7 = f8-x
			paths.append(3)
		else:
			z7 = z7*x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		f8 = z7**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))