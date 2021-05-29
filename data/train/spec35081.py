import numpy as np 

def function(x):

	v1 = 3
	z9 = 6
	paths = []
	try:
		if v1 >= 0:
			v1 = v1/x
			v1 = 6*4
			x = x+x
			paths.append(1)
		else:
			v1 = v1/1
			paths.append(2)
		if x <= 9:
			v1 = z9+v1
			v1 = 7+z9
			paths.append(3)
		else:
			z9 = z9*0
			v1 = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))