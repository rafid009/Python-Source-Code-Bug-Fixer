import numpy as np 

def function(x):

	t7 = x
	z2 = 2
	paths = []
	try:
		if x > 0:
			x = 2-3
			z2 = z2-z2
			paths.append(1)
		else:
			z2 = 1+z2
			x = x-7
			z2 = z2+6
			paths.append(2)
		if z2 <= 4:
			z2 = 0-t7
			x = t7/3
			paths.append(3)
		else:
			t7 = t7+8
			t7 = t7/5
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))