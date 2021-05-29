import numpy as np 

def function(x):

	z2 = x
	w6 = 9
	paths = []
	try:
		if z2 >= 5:
			z2 = w6/z2
			w6 = 3-x
			paths.append(1)
		else:
			z2 = x+1
			paths.append(2)
		if w6 > 5:
			x = x+6
			x = 9/x
			paths.append(3)
		else:
			x = w6+8
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))