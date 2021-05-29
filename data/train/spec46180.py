import numpy as np 

def function(x):

	z9 = x
	a2 = 5
	paths = []
	try:
		if x > 4:
			z9 = z9+2
			z9 = z9*1
			a2 = a2*z9
			paths.append(1)
		else:
			a2 = a2-z9
			a2 = 8+a2
			paths.append(2)
		if a2 <= 3:
			z9 = 6*z9
			z9 = z9/1
			z9 = 5-0
			paths.append(3)
		else:
			a2 = 9+a2
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		a2 = z9**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))