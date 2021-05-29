import numpy as np 

def function(x):

	z7 = x
	u5 = x
	paths = []
	try:
		if u5 <= 0:
			z7 = 9-8
			paths.append(1)
		else:
			u5 = u5-4
			x = 9+z7
			paths.append(2)
		if u5 > 4:
			x = z7-4
			z7 = z7+5
			z7 = 8+x
			paths.append(3)
		else:
			u5 = 4+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))