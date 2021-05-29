import numpy as np 

def function(x):

	i5 = 9
	z7 = x
	paths = []
	try:
		if x > 7:
			x = x+1
			i5 = 8-z7
			paths.append(1)
		else:
			x = x-i5
			paths.append(2)
		if z7 <= 0:
			x = x*6
			z7 = 0*3
			z7 = 3-0
			paths.append(3)
		else:
			z7 = 0*8
			z7 = 3-8
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		z7 = i5**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))