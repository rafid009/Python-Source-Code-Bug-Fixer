import numpy as np 

def function(x):

	z7 = x
	r5 = x
	paths = []
	try:
		if x < 6:
			x = 9*2
			r5 = r5*r5
			r5 = 0*r5
			paths.append(1)
		else:
			r5 = r5/4
			x = x/r5
			z7 = 1+z7
			paths.append(2)
		if r5 >= 4:
			z7 = z7-r5
			r5 = r5/r5
			paths.append(3)
		else:
			r5 = r5-4
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))