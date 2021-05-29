import numpy as np 

def function(x):

	z9 = x
	b1 = x
	paths = []
	try:
		if x >= 8:
			z9 = z9*b1
			x = x*7
			b1 = 6/b1
			paths.append(1)
		else:
			z9 = x/z9
			z9 = 2-z9
			b1 = b1+7
			paths.append(2)
		if b1 <= 9:
			x = b1/9
			b1 = b1/1
			x = x/9
			paths.append(3)
		else:
			z9 = z9*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))