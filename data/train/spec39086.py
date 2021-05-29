import numpy as np 

def function(x):

	j9 = x
	z9 = x
	paths = []
	try:
		if x <= 1:
			j9 = j9*5
			x = x/2
			paths.append(1)
		else:
			z9 = 2+z9
			z9 = z9/z9
			z9 = 2*z9
			paths.append(2)
		if z9 > 4:
			j9 = x*x
			paths.append(3)
		else:
			x = z9/6
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))