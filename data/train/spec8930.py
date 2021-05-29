import numpy as np 

def function(x):

	f4 = 3
	z4 = x
	paths = []
	try:
		if x < 8:
			z4 = z4+9
			paths.append(1)
		else:
			f4 = 0/z4
			paths.append(2)
		if f4 <= 8:
			f4 = 5-f4
			paths.append(3)
		else:
			f4 = 5/x
			f4 = 4/f4
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