import numpy as np 

def function(x):

	z9 = x
	paths = []
	try:
		if z9 <= 7:
			x = 1/x
			paths.append(1)
		else:
			x = 4*8
			x = x*z9
			paths.append(2)
		if z9 < 9:
			x = 7+z9
			x = 3+x
			paths.append(3)
		else:
			x = x+z9
			z9 = x-z9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))