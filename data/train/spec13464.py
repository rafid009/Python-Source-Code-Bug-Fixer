import numpy as np 

def function(x):

	w2 = x
	z8 = 3
	paths = []
	try:
		if z8 <= 4:
			z8 = x+z8
			x = x*8
			paths.append(1)
		else:
			z8 = z8/x
			paths.append(2)
		if z8 > 5:
			z8 = z8+1
			paths.append(3)
		else:
			x = 8+x
			z8 = z8+z8
			x = x+7
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		w2 = z8**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))