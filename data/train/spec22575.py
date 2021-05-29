import numpy as np 

def function(x):

	r7 = x
	z9 = 2
	paths = []
	try:
		if z9 > 1:
			z9 = r7/z9
			z9 = 0+r7
			x = x-0
			paths.append(1)
		else:
			r7 = r7+x
			x = x-8
			paths.append(2)
		if x < 2:
			z9 = z9+8
			paths.append(3)
		else:
			r7 = 8+2
			z9 = z9/x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))