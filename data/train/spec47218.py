import numpy as np 

def function(x):

	z5 = 4
	f7 = 5
	paths = []
	try:
		if f7 >= 5:
			z5 = 1+9
			paths.append(1)
		else:
			f7 = f7*3
			paths.append(2)
		if z5 < 5:
			f7 = z5+4
			paths.append(3)
		else:
			f7 = 8*f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))