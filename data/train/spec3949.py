import numpy as np 

def function(x):

	r1 = x
	z4 = 6
	x = x
	paths = []
	try:
		if z4 >= 1:
			z4 = r1+6
			z4 = z4-x
			z4 = z4*1
			paths.append(1)
		else:
			z4 = z4+0
			paths.append(2)
		if x > 8:
			z4 = 6-4
			r1 = z4-0
			r1 = 1+r1
			paths.append(3)
		else:
			z4 = z4/9
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))