import numpy as np 

def function(x):

	z7 = 9
	r8 = x
	paths = []
	try:
		if r8 >= 9:
			x = 2*x
			x = 2+x
			x = 7*x
			paths.append(1)
		else:
			r8 = x*6
			paths.append(2)
		if z7 >= 9:
			x = 3+x
			x = 1-x
			paths.append(3)
		else:
			z7 = r8/z7
			r8 = r8+1
			r8 = 3*r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		z7 = r8**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))