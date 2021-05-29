import numpy as np 

def function(x):

	z9 = x
	n8 = 5
	x = 6
	paths = []
	try:
		if x > 1:
			n8 = 3*z9
			x = 0-x
			n8 = 0*2
			paths.append(1)
		else:
			x = 2-1
			n8 = n8-n8
			paths.append(2)
		if z9 > 3:
			z9 = 2*z9
			paths.append(3)
		else:
			x = x/1
			z9 = z9-2
			n8 = 1/x
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		n8 = z9**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))