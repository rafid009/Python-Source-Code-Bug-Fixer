import numpy as np 

def function(x):

	z6 = 4
	t8 = 6
	paths = []
	try:
		if t8 > 6:
			t8 = 9*9
			x = x/8
			paths.append(1)
		else:
			x = t8*x
			paths.append(2)
		if t8 <= 1:
			z6 = z6-1
			paths.append(3)
		else:
			x = x+z6
			z6 = 4*8
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))