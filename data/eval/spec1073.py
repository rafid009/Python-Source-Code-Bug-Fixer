import numpy as np 

def function(x):

	j1 = x
	z9 = 1
	paths = []
	try:
		if z9 > 4:
			z9 = z9*x
			paths.append(1)
		else:
			z9 = j1/6
			z9 = x-2
			paths.append(2)
		if x <= 1:
			z9 = j1/j1
			paths.append(3)
		else:
			x = 3+x
			z9 = z9*9
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		z9 = j1**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))