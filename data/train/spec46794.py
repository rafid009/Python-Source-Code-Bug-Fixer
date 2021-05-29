import numpy as np 

def function(x):

	z5 = 8
	f9 = 3
	x = x
	paths = []
	try:
		if x <= 5:
			f9 = f9-x
			x = 7*x
			paths.append(1)
		else:
			z5 = 3-z5
			paths.append(2)
		if x >= 4:
			x = 7-f9
			paths.append(3)
		else:
			f9 = x-x
			z5 = 8*3
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))