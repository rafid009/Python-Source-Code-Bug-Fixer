import numpy as np 

def function(x):

	y3 = 9
	z6 = 1
	paths = []
	try:
		if x <= 9:
			y3 = 6-7
			paths.append(1)
		else:
			x = y3-8
			y3 = y3+y3
			z6 = z6+5
			paths.append(2)
		if x > 7:
			x = z6+2
			z6 = y3-8
			x = 2-1
			paths.append(3)
		else:
			x = z6/x
			z6 = 8*y3
			z6 = x*z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		y3 = z6**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))