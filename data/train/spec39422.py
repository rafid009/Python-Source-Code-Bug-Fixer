import numpy as np 

def function(x):

	z2 = 9
	r8 = x
	paths = []
	try:
		if x > 7:
			x = 0*x
			x = 2*3
			r8 = r8*0
			paths.append(1)
		else:
			z2 = 4+z2
			z2 = 6+z2
			paths.append(2)
		if z2 < 8:
			z2 = z2-4
			x = x*6
			paths.append(3)
		else:
			z2 = x-z2
			x = x+r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))