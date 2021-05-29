import numpy as np 

def function(x):

	z9 = 9
	w9 = x
	paths = []
	try:
		if x <= 3:
			x = w9*0
			paths.append(1)
		else:
			w9 = 7+4
			z9 = 2-z9
			paths.append(2)
		if w9 <= 4:
			x = 5-4
			paths.append(3)
		else:
			x = x/8
			x = x*z9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))