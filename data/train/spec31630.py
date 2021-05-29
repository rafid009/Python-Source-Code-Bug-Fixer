import numpy as np 

def function(x):

	z7 = x
	t1 = x
	paths = []
	try:
		if x > 3:
			z7 = 2+z7
			x = x-1
			paths.append(1)
		else:
			z7 = z7-4
			paths.append(2)
		if x <= 7:
			z7 = t1*6
			x = 0*x
			paths.append(3)
		else:
			t1 = t1+5
			x = 5+9
			x = 7/x
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