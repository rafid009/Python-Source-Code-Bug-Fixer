import numpy as np 

def function(x):

	z9 = x
	j9 = x
	paths = []
	try:
		if z9 < 5:
			z9 = 4+z9
			paths.append(1)
		else:
			z9 = z9+j9
			x = 0-x
			paths.append(2)
		if z9 <= 4:
			z9 = z9+j9
			paths.append(3)
		else:
			j9 = x-2
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		j9 = z9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))