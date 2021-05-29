import numpy as np 

def function(x):

	z5 = x
	n3 = 9
	paths = []
	try:
		if n3 < 9:
			x = 8*x
			n3 = n3/n3
			paths.append(1)
		else:
			x = x/3
			n3 = n3+1
			paths.append(2)
		if x >= 9:
			z5 = z5*4
			x = x*6
			paths.append(3)
		else:
			x = x+n3
			x = x*5
			n3 = n3*4
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		n3 = z5**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))