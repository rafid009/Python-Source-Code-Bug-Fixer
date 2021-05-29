import numpy as np 

def function(x):

	z1 = 6
	b8 = x
	paths = []
	try:
		if x <= 3:
			z1 = z1*9
			paths.append(1)
		else:
			x = 3+5
			x = z1-x
			b8 = b8-x
			paths.append(2)
		if b8 >= 7:
			b8 = b8+7
			x = x*6
			x = x/b8
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))