import numpy as np 

def function(x):

	z2 = 4
	r4 = x
	paths = []
	try:
		if r4 > 5:
			r4 = 6/r4
			paths.append(1)
		else:
			r4 = r4+r4
			paths.append(2)
		if x >= 4:
			r4 = r4+1
			paths.append(3)
		else:
			z2 = 5+8
			z2 = z2/3
			z2 = z2+5
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))