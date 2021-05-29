import numpy as np 

def function(x):

	r8 = 5
	z2 = 1
	paths = []
	try:
		if x <= 5:
			z2 = z2-4
			z2 = z2-r8
			paths.append(1)
		else:
			r8 = x+2
			x = 3/8
			r8 = 2/r8
			paths.append(2)
		if r8 > 0:
			x = 4-x
			x = 7-2
			x = x-6
			paths.append(3)
		else:
			x = r8+7
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		r8 = z2**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))