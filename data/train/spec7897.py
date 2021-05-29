import numpy as np 

def function(x):

	e5 = x
	z6 = x
	paths = []
	try:
		if x <= 5:
			e5 = 5/8
			x = 0-x
			e5 = e5-z6
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if z6 > 0:
			e5 = e5*1
			x = 8*8
			x = e5+1
			paths.append(3)
		else:
			z6 = z6*x
			e5 = e5*3
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))