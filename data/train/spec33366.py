import numpy as np 

def function(x):

	z9 = 2
	w1 = 9
	paths = []
	try:
		if x < 2:
			x = 9*x
			paths.append(1)
		else:
			x = x+6
			z9 = 9+w1
			paths.append(2)
		if z9 <= 7:
			w1 = 2-0
			z9 = z9-8
			paths.append(3)
		else:
			z9 = z9*z9
			x = x*4
			x = 7*x
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