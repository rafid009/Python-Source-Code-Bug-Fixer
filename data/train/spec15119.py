import numpy as np 

def function(x):

	f4 = x
	z6 = x
	paths = []
	try:
		if f4 >= 7:
			z6 = 3/4
			paths.append(1)
		else:
			f4 = f4-f4
			paths.append(2)
		if z6 >= 5:
			f4 = 1*3
			paths.append(3)
		else:
			f4 = f4*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))