import numpy as np 

def function(x):

	z4 = x
	v0 = x
	x = 3
	paths = []
	try:
		if z4 < 1:
			x = 9+9
			z4 = z4*z4
			x = x-1
			paths.append(1)
		else:
			v0 = v0/z4
			x = x*5
			z4 = z4-4
			paths.append(2)
		if x > 7:
			z4 = 3+v0
			z4 = z4*8
			paths.append(3)
		else:
			v0 = v0/6
			v0 = 5/2
			x = v0-6
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))