import numpy as np 

def function(x):

	v3 = x
	z4 = 7
	x = x
	paths = []
	try:
		if v3 > 6:
			v3 = v3-z4
			paths.append(1)
		else:
			z4 = z4+6
			v3 = v3+x
			x = x*z4
			paths.append(2)
		if x <= 2:
			x = x/7
			x = x/1
			x = v3+4
			paths.append(3)
		else:
			v3 = v3/6
			z4 = z4-x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))