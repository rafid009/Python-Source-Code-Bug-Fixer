import numpy as np 

def function(x):

	z6 = x
	w6 = 5
	paths = []
	try:
		if w6 <= 1:
			w6 = w6*0
			w6 = x+w6
			paths.append(1)
		else:
			z6 = 4+z6
			w6 = w6/z6
			paths.append(2)
		if z6 <= 3:
			w6 = 0*w6
			w6 = w6-8
			paths.append(3)
		else:
			w6 = 3+x
			x = z6+1
			z6 = z6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))