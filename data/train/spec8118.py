import numpy as np 

def function(x):

	n7 = 9
	z6 = x
	paths = []
	try:
		if n7 > 8:
			n7 = 0*n7
			n7 = n7+2
			paths.append(1)
		else:
			x = 0+x
			z6 = 5*x
			x = 7+1
			paths.append(2)
		if n7 > 5:
			z6 = 6+z6
			x = x*1
			n7 = 6/5
			paths.append(3)
		else:
			z6 = z6-7
			z6 = z6-3
			n7 = x+7
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))