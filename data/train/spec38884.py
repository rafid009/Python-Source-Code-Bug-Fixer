import numpy as np 

def function(x):

	t9 = x
	z2 = 6
	paths = []
	try:
		if x > 5:
			x = z2/1
			z2 = 5-z2
			t9 = 1*t9
			paths.append(1)
		else:
			z2 = 6*z2
			x = x/9
			t9 = 4-8
			paths.append(2)
		if t9 > 1:
			z2 = z2+z2
			x = z2/x
			t9 = 7*z2
			paths.append(3)
		else:
			z2 = z2*1
			t9 = z2-t9
			z2 = z2+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))