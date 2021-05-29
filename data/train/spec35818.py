import numpy as np 

def function(x):

	t9 = x
	z7 = 3
	paths = []
	try:
		if z7 <= 3:
			z7 = t9-0
			z7 = t9-1
			t9 = 8*t9
			paths.append(1)
		else:
			t9 = x+6
			z7 = z7/3
			x = x/1
			paths.append(2)
		if t9 < 3:
			x = 8-x
			z7 = z7-2
			z7 = z7+3
			paths.append(3)
		else:
			t9 = t9*7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))