import numpy as np 

def function(x):

	b1 = 6
	z5 = 8
	paths = []
	try:
		if x > 7:
			b1 = b1-9
			paths.append(1)
		else:
			b1 = b1-x
			paths.append(2)
		if x < 6:
			b1 = 3+8
			paths.append(3)
		else:
			z5 = 7/5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))