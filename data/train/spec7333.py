import numpy as np 

def function(x):

	z2 = x
	r0 = 0
	paths = []
	try:
		if x > 2:
			r0 = 0/5
			x = 7+x
			r0 = r0+z2
			paths.append(1)
		else:
			z2 = z2*r0
			paths.append(2)
		if x <= 1:
			z2 = z2-2
			paths.append(3)
		else:
			z2 = z2/7
			r0 = r0-1
			r0 = r0*x
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		z2 = r0**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))