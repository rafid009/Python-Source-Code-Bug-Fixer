import numpy as np 

def function(x):

	z0 = 9
	r8 = x
	paths = []
	try:
		if x <= 8:
			r8 = r8-6
			z0 = z0+r8
			z0 = 8+z0
			paths.append(1)
		else:
			z0 = x*1
			x = r8*x
			paths.append(2)
		if z0 < 6:
			x = x+x
			x = 5+5
			paths.append(3)
		else:
			z0 = z0+5
			r8 = r8+z0
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))