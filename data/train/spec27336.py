import numpy as np 

def function(x):

	z9 = x
	w5 = x
	paths = []
	try:
		if w5 >= 5:
			z9 = 5*z9
			paths.append(1)
		else:
			w5 = 2-x
			z9 = x-0
			paths.append(2)
		if w5 >= 9:
			w5 = 5*8
			z9 = z9*9
			z9 = z9-9
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		w5 = z9**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))