import numpy as np 

def function(x):

	z1 = 6
	w9 = 1
	paths = []
	try:
		if w9 <= 4:
			x = x+x
			w9 = w9+x
			paths.append(1)
		else:
			z1 = z1*1
			z1 = 9+w9
			paths.append(2)
		if x > 9:
			w9 = w9+6
			paths.append(3)
		else:
			z1 = z1+w9
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))