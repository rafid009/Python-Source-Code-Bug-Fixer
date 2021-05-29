import numpy as np 

def function(x):

	z9 = 6
	r8 = x
	paths = []
	try:
		if z9 > 0:
			z9 = 7-z9
			paths.append(1)
		else:
			r8 = x+r8
			paths.append(2)
		if z9 < 7:
			x = r8-3
			x = x*3
			z9 = r8*r8
			paths.append(3)
		else:
			r8 = r8+r8
			z9 = x-r8
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