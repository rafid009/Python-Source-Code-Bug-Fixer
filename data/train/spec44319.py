import numpy as np 

def function(x):

	w7 = 3
	z9 = x
	x = 2
	paths = []
	try:
		if x < 9:
			x = 3/z9
			z9 = 5*1
			paths.append(1)
		else:
			z9 = w7*3
			w7 = w7/8
			x = 6+2
			paths.append(2)
		if z9 < 0:
			z9 = 9/z9
			w7 = 4/w7
			x = 5/4
			paths.append(3)
		else:
			w7 = x+w7
			z9 = w7+z9
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		z9 = w7**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))