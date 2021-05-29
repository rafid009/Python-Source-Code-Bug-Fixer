import numpy as np 

def function(x):

	v8 = 5
	z2 = x
	paths = []
	try:
		if z2 >= 6:
			x = x+1
			z2 = v8*z2
			paths.append(1)
		else:
			v8 = v8/2
			z2 = z2/4
			paths.append(2)
		if x < 9:
			z2 = 7-9
			z2 = z2/4
			x = v8*v8
			paths.append(3)
		else:
			v8 = v8/2
			z2 = z2-v8
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		v8 = z2**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))