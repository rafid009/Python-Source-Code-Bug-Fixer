import numpy as np 

def function(x):

	z2 = x
	t7 = 2
	paths = []
	try:
		if x < 7:
			t7 = t7-9
			z2 = x+z2
			x = 6/t7
			paths.append(1)
		else:
			z2 = 1-z2
			x = 6-x
			z2 = 2*6
			paths.append(2)
		if t7 < 8:
			z2 = z2*4
			z2 = z2+t7
			t7 = t7*x
			paths.append(3)
		else:
			x = 3+2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		t7 = z2**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))