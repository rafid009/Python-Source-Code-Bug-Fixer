import numpy as np 

def function(x):

	z2 = 5
	r2 = x
	paths = []
	try:
		if r2 <= 3:
			r2 = 6-r2
			x = x/1
			x = 6*z2
			paths.append(1)
		else:
			z2 = r2-5
			z2 = z2/2
			x = x*x
			paths.append(2)
		if z2 > 7:
			r2 = r2+4
			z2 = z2/3
			paths.append(3)
		else:
			r2 = r2-z2
			x = 4*x
			z2 = z2-x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))