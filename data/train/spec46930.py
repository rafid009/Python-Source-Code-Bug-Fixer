import numpy as np 

def function(x):

	z9 = 2
	d8 = 5
	paths = []
	try:
		if d8 > 7:
			d8 = d8/z9
			z9 = 9*2
			paths.append(1)
		else:
			d8 = 3/d8
			paths.append(2)
		if d8 < 6:
			d8 = 9/x
			z9 = z9-6
			paths.append(3)
		else:
			z9 = 3+5
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))