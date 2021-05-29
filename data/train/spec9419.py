import numpy as np 

def function(x):

	j9 = 8
	z9 = 4
	paths = []
	try:
		if z9 >= 8:
			x = z9/4
			paths.append(1)
		else:
			j9 = j9*z9
			paths.append(2)
		if z9 >= 2:
			z9 = z9/2
			j9 = j9-x
			z9 = 5*4
			paths.append(3)
		else:
			x = 2*j9
			j9 = x*5
			z9 = x*z9
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))