import numpy as np 

def function(x):

	z2 = x
	l2 = 0
	paths = []
	try:
		if x <= 3:
			l2 = 3+4
			x = 0+x
			x = x*l2
			paths.append(1)
		else:
			l2 = l2*0
			z2 = z2-3
			x = x*2
			paths.append(2)
		if z2 > 0:
			x = 8*x
			l2 = 4-1
			paths.append(3)
		else:
			z2 = x-z2
			z2 = z2*7
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))