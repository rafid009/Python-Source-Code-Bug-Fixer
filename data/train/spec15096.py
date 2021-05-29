import numpy as np 

def function(x):

	r1 = x
	z1 = 9
	paths = []
	try:
		if x < 9:
			x = r1-3
			r1 = r1*6
			paths.append(1)
		else:
			z1 = 5+z1
			paths.append(2)
		if x >= 7:
			x = x/x
			x = 1+x
			z1 = z1+3
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))