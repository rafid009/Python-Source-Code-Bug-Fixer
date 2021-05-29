import numpy as np 

def function(x):

	z9 = x
	w5 = x
	paths = []
	try:
		if x > 6:
			x = x+x
			w5 = w5-w5
			paths.append(1)
		else:
			w5 = 2+w5
			paths.append(2)
		if z9 >= 7:
			x = z9-x
			z9 = 2/9
			paths.append(3)
		else:
			z9 = 9*w5
			z9 = z9*3
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