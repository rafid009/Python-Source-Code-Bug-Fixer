import numpy as np 

def function(x):

	i6 = x
	z9 = x
	x = 8
	paths = []
	try:
		if x < 9:
			i6 = i6*4
			i6 = 7*6
			i6 = 5-i6
			paths.append(1)
		else:
			x = i6+8
			i6 = z9+x
			paths.append(2)
		if x >= 8:
			i6 = i6/i6
			z9 = z9+4
			x = x*6
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))