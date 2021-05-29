import numpy as np 

def function(x):

	v2 = x
	z7 = x
	paths = []
	try:
		if z7 <= 5:
			v2 = v2-4
			paths.append(1)
		else:
			v2 = 7-8
			paths.append(2)
		if z7 <= 4:
			z7 = 2-z7
			paths.append(3)
		else:
			z7 = z7-z7
			v2 = 9+x
			x = z7+v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))