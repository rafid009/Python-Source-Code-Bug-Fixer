import numpy as np 

def function(x):

	z7 = x
	b6 = x
	paths = []
	try:
		if b6 <= 1:
			x = x*2
			b6 = 2-b6
			z7 = z7-2
			paths.append(1)
		else:
			x = 9+z7
			b6 = b6/b6
			paths.append(2)
		if x <= 4:
			x = 5*x
			z7 = z7*8
			paths.append(3)
		else:
			b6 = z7+x
			z7 = 3/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))