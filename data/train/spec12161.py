import numpy as np 

def function(x):

	z7 = 1
	r8 = x
	paths = []
	try:
		if r8 < 2:
			r8 = r8-z7
			z7 = x-r8
			x = 4+x
			paths.append(1)
		else:
			r8 = r8-z7
			paths.append(2)
		if x <= 2:
			z7 = 7+x
			x = z7+7
			paths.append(3)
		else:
			z7 = r8*4
			x = z7+x
			z7 = r8*z7
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