import numpy as np 

def function(x):

	i1 = x
	z2 = 8
	paths = []
	try:
		if z2 > 8:
			x = 5*x
			z2 = 9*i1
			paths.append(1)
		else:
			i1 = z2/i1
			z2 = i1-x
			x = x*5
			paths.append(2)
		if i1 <= 2:
			i1 = i1-3
			i1 = x+1
			z2 = z2+3
			paths.append(3)
		else:
			i1 = x*z2
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))