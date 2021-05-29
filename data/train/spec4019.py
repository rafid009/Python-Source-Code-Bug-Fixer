import numpy as np 

def function(x):

	t7 = 0
	z6 = x
	x = x
	paths = []
	try:
		if x >= 5:
			t7 = z6*t7
			z6 = z6-9
			paths.append(1)
		else:
			z6 = z6/1
			z6 = z6/5
			paths.append(2)
		if z6 <= 6:
			x = x/2
			paths.append(3)
		else:
			z6 = 5*4
			t7 = t7-5
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))