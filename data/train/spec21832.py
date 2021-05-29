import numpy as np 

def function(x):

	z4 = x
	v2 = 5
	paths = []
	try:
		if z4 < 7:
			v2 = v2+8
			v2 = 3-8
			v2 = v2+9
			paths.append(1)
		else:
			v2 = 4*0
			z4 = z4/z4
			paths.append(2)
		if x >= 0:
			z4 = v2*6
			paths.append(3)
		else:
			v2 = z4*9
			v2 = 7/1
			z4 = 2*v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))