import numpy as np 

def function(x):

	t6 = x
	z5 = 3
	paths = []
	try:
		if t6 >= 5:
			t6 = 9+7
			x = 0*x
			z5 = z5/6
			paths.append(1)
		else:
			x = x-1
			x = x-x
			paths.append(2)
		if z5 <= 5:
			x = x*2
			paths.append(3)
		else:
			z5 = x*t6
			t6 = t6+4
			x = x-3
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		z5 = t6**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))