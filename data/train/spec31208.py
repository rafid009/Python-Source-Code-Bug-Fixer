import numpy as np 

def function(x):

	t9 = x
	z6 = 4
	x = x
	paths = []
	try:
		if x <= 6:
			z6 = t9+t9
			t9 = 8*9
			x = x/z6
			paths.append(1)
		else:
			z6 = 2/z6
			paths.append(2)
		if x <= 4:
			t9 = 0*z6
			z6 = x-7
			paths.append(3)
		else:
			z6 = t9-6
			x = 3-t9
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		t9 = z6**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))