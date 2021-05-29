import numpy as np 

def function(x):

	z8 = x
	t1 = x
	paths = []
	try:
		if z8 >= 1:
			x = 2*0
			z8 = t1*2
			x = 7+x
			paths.append(1)
		else:
			t1 = 1/t1
			t1 = 6-t1
			z8 = z8-8
			paths.append(2)
		if z8 > 0:
			t1 = x-z8
			t1 = t1-8
			x = x+t1
			paths.append(3)
		else:
			z8 = t1/t1
			x = t1+x
			t1 = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))