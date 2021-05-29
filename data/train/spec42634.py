import numpy as np 

def function(x):

	z9 = x
	j0 = x
	paths = []
	try:
		if z9 <= 7:
			z9 = j0+1
			j0 = j0+j0
			j0 = 3/j0
			paths.append(1)
		else:
			j0 = 6-j0
			z9 = z9/5
			paths.append(2)
		if x <= 0:
			x = x/6
			j0 = 5+8
			paths.append(3)
		else:
			j0 = 4*x
			j0 = j0*j0
			z9 = 2*3
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