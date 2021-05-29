import numpy as np 

def function(x):

	j6 = 3
	z9 = x
	paths = []
	try:
		if j6 <= 9:
			x = x*j6
			z9 = z9+4
			z9 = z9/8
			paths.append(1)
		else:
			z9 = z9/5
			j6 = 7+j6
			j6 = x-z9
			paths.append(2)
		if j6 <= 3:
			x = 6/x
			paths.append(3)
		else:
			j6 = j6*x
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