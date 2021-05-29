import numpy as np 

def function(x):

	n5 = 1
	z4 = x
	paths = []
	try:
		if x < 6:
			x = x+6
			x = 5+x
			paths.append(1)
		else:
			n5 = n5+n5
			z4 = z4*2
			x = 5+1
			paths.append(2)
		if z4 <= 8:
			n5 = z4-n5
			paths.append(3)
		else:
			z4 = z4-z4
			n5 = n5*1
			x = x/4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		n5 = z4**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))