import numpy as np 

def function(x):

	j3 = x
	z9 = 3
	x = x
	paths = []
	try:
		if x <= 2:
			z9 = 4/z9
			paths.append(1)
		else:
			x = z9+4
			j3 = 8/9
			paths.append(2)
		if j3 > 4:
			x = x+5
			paths.append(3)
		else:
			z9 = 2/j3
			j3 = j3*4
			j3 = j3-7
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