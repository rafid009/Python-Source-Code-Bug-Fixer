import numpy as np 

def function(x):

	b0 = 7
	z6 = 2
	paths = []
	try:
		if b0 >= 6:
			x = x/z6
			z6 = 8+z6
			paths.append(1)
		else:
			x = 8*7
			z6 = z6-b0
			paths.append(2)
		if b0 <= 9:
			z6 = z6/6
			b0 = 6+1
			paths.append(3)
		else:
			b0 = z6-2
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))