import numpy as np 

def function(x):

	e7 = x
	z1 = 6
	paths = []
	try:
		if e7 <= 6:
			e7 = z1+9
			x = x*6
			paths.append(1)
		else:
			e7 = e7/7
			paths.append(2)
		if e7 < 6:
			x = x*7
			x = 4-8
			paths.append(3)
		else:
			x = x/4
			x = x*8
			z1 = x*7
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))