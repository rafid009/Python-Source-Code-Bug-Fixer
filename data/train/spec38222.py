import numpy as np 

def function(x):

	b4 = 9
	z4 = 2
	paths = []
	try:
		if b4 > 3:
			b4 = b4*8
			b4 = x/3
			b4 = 5-3
			paths.append(1)
		else:
			z4 = z4+1
			paths.append(2)
		if b4 >= 7:
			b4 = z4+4
			x = x+8
			z4 = 8*4
			paths.append(3)
		else:
			z4 = 5-x
			z4 = b4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))