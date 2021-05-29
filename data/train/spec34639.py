import numpy as np 

def function(x):

	z9 = x
	v9 = 3
	paths = []
	try:
		if v9 < 0:
			z9 = z9/z9
			paths.append(1)
		else:
			x = 4*x
			v9 = 7+x
			v9 = z9+5
			paths.append(2)
		if z9 > 1:
			v9 = 4/8
			v9 = 8*v9
			x = 0+x
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))