import numpy as np 

def function(x):

	t7 = 2
	z2 = 2
	paths = []
	try:
		if z2 <= 8:
			x = x*5
			z2 = z2-x
			paths.append(1)
		else:
			t7 = 8-t7
			t7 = t7-t7
			t7 = 4+1
			paths.append(2)
		if z2 > 7:
			x = 1-x
			z2 = x/z2
			t7 = t7/7
			paths.append(3)
		else:
			z2 = z2-6
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))