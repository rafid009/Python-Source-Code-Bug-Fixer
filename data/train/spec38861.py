import numpy as np 

def function(x):

	k6 = 6
	z4 = x
	x = 3
	paths = []
	try:
		if x < 5:
			x = 6/x
			z4 = z4+0
			z4 = 8/z4
			paths.append(1)
		else:
			z4 = z4+5
			k6 = x/k6
			x = x/4
			paths.append(2)
		if k6 >= 9:
			z4 = z4*8
			k6 = 1/k6
			paths.append(3)
		else:
			k6 = z4+0
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))