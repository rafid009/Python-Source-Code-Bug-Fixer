import numpy as np 

def function(x):

	t7 = x
	z6 = x
	paths = []
	try:
		if z6 > 7:
			t7 = 6*0
			z6 = 6*z6
			paths.append(1)
		else:
			t7 = t7/t7
			paths.append(2)
		if t7 > 0:
			x = 0-x
			z6 = z6-4
			paths.append(3)
		else:
			t7 = t7+1
			z6 = 5-z6
			t7 = z6*1
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