import numpy as np 

def function(x):

	n3 = 9
	z7 = 2
	paths = []
	try:
		if x <= 5:
			n3 = x+8
			z7 = 2*z7
			x = x*2
			paths.append(1)
		else:
			n3 = n3/n3
			x = 7-1
			paths.append(2)
		if n3 <= 9:
			x = z7-8
			n3 = z7/4
			n3 = x*1
			paths.append(3)
		else:
			x = x*4
			n3 = 6/n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))