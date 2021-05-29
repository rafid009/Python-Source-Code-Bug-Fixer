import numpy as np 

def function(x):

	z4 = x
	f8 = 2
	paths = []
	try:
		if x <= 8:
			x = x*9
			paths.append(1)
		else:
			z4 = 8-z4
			paths.append(2)
		if x <= 5:
			x = x/6
			z4 = 4-z4
			paths.append(3)
		else:
			x = 6/7
			f8 = f8-6
			x = x*f8
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))