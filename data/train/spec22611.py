import numpy as np 

def function(x):

	z9 = 5
	w2 = 9
	paths = []
	try:
		if w2 >= 1:
			w2 = 7*x
			z9 = z9-8
			paths.append(1)
		else:
			z9 = 4/z9
			w2 = w2/x
			z9 = z9*1
			paths.append(2)
		if z9 >= 3:
			x = 2*x
			paths.append(3)
		else:
			w2 = 9*w2
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		z9 = w2**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))