import numpy as np 

def function(x):

	n1 = 8
	z4 = x
	paths = []
	try:
		if z4 <= 5:
			z4 = 1+z4
			paths.append(1)
		else:
			z4 = 1/z4
			n1 = x-7
			paths.append(2)
		if n1 >= 7:
			x = x+9
			paths.append(3)
		else:
			x = x*0
			x = 3/8
			x = x*3
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		z4 = n1**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))