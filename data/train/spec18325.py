import numpy as np 

def function(x):

	b6 = 8
	z9 = 2
	paths = []
	try:
		if z9 <= 8:
			b6 = z9-6
			x = x/x
			z9 = b6*1
			paths.append(1)
		else:
			b6 = b6+x
			b6 = 4-2
			paths.append(2)
		if z9 > 1:
			x = x+b6
			x = 0+5
			z9 = z9+z9
			paths.append(3)
		else:
			b6 = 2*b6
			x = 2-x
			z9 = z9*x
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))