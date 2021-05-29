import numpy as np 

def function(x):

	b3 = 4
	z5 = 1
	paths = []
	try:
		if x > 8:
			x = x-1
			b3 = b3+5
			b3 = b3-b3
			paths.append(1)
		else:
			z5 = z5-2
			x = 6-6
			paths.append(2)
		if z5 < 5:
			x = 8-0
			b3 = b3*7
			paths.append(3)
		else:
			z5 = 0/z5
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		b3 = z5**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))