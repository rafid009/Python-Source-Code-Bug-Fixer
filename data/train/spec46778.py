import numpy as np 

def function(x):

	z9 = x
	w3 = x
	x = 6
	paths = []
	try:
		if z9 <= 0:
			x = 2+1
			w3 = w3/4
			paths.append(1)
		else:
			z9 = 5-z9
			z9 = w3*z9
			paths.append(2)
		if z9 >= 3:
			w3 = 7+w3
			paths.append(3)
		else:
			z9 = z9-z9
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		w3 = w3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))