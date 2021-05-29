import numpy as np 

def function(x):

	z8 = x
	f4 = 8
	paths = []
	try:
		if f4 >= 2:
			x = x-8
			paths.append(1)
		else:
			x = x*f4
			paths.append(2)
		if f4 <= 4:
			f4 = f4+x
			paths.append(3)
		else:
			z8 = 2+6
			z8 = x/4
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		f4 = z8**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))