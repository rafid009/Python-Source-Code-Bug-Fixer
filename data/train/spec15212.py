import numpy as np 

def function(x):

	z6 = 3
	n7 = 4
	paths = []
	try:
		if x < 4:
			x = 0+x
			paths.append(1)
		else:
			z6 = 7*z6
			n7 = 2-n7
			paths.append(2)
		if n7 <= 4:
			z6 = z6-x
			n7 = n7-x
			paths.append(3)
		else:
			n7 = n7/8
			x = 2+0
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))