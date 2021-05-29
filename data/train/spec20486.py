import numpy as np 

def function(x):

	r3 = 4
	z1 = x
	paths = []
	try:
		if z1 < 6:
			x = 3+x
			x = 1*9
			paths.append(1)
		else:
			x = x+3
			x = z1-x
			r3 = 0*r3
			paths.append(2)
		if r3 < 7:
			x = x+4
			x = z1-x
			paths.append(3)
		else:
			z1 = z1/z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		r3 = z1**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))