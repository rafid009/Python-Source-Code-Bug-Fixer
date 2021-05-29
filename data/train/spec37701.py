import numpy as np 

def function(x):

	z9 = x
	x6 = x
	paths = []
	try:
		if x > 1:
			x = 5-4
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x < 2:
			x6 = x6*9
			x = z9*x
			z9 = z9*0
			paths.append(3)
		else:
			x = z9*1
			z9 = z9/z9
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))