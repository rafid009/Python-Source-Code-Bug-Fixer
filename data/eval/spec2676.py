import numpy as np 

def function(x):

	v8 = x
	z8 = x
	paths = []
	try:
		if x <= 9:
			v8 = 0*8
			x = v8*3
			paths.append(1)
		else:
			z8 = z8/7
			z8 = 6*z8
			v8 = 0-v8
			paths.append(2)
		if x >= 4:
			z8 = 8-z8
			v8 = x*1
			z8 = 3/z8
			paths.append(3)
		else:
			v8 = z8+x
			x = z8-5
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		z8 = v8**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))