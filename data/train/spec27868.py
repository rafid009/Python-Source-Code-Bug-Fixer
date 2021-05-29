import numpy as np 

def function(x):

	z6 = x
	w4 = 5
	paths = []
	try:
		if w4 <= 3:
			w4 = 4/6
			w4 = 7+2
			z6 = 4+z6
			paths.append(1)
		else:
			z6 = 2-z6
			paths.append(2)
		if x > 7:
			z6 = z6-6
			x = x-1
			paths.append(3)
		else:
			w4 = 2-w4
			x = x*1
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		w4 = z6**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))