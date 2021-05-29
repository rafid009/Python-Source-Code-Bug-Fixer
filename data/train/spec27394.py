import numpy as np 

def function(x):

	z5 = x
	a9 = 3
	paths = []
	try:
		if a9 <= 6:
			z5 = x*8
			paths.append(1)
		else:
			a9 = a9+3
			z5 = x+0
			paths.append(2)
		if x <= 9:
			a9 = 0+x
			x = x*1
			x = x/3
			paths.append(3)
		else:
			x = x*8
			z5 = z5/a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))