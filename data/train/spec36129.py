import numpy as np 

def function(x):

	y1 = 5
	z9 = x
	x = 6
	paths = []
	try:
		if z9 <= 7:
			x = x/x
			paths.append(1)
		else:
			y1 = y1+y1
			y1 = 4/y1
			x = x-3
			paths.append(2)
		if x > 4:
			x = x/6
			z9 = 2-z9
			paths.append(3)
		else:
			y1 = 9-y1
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))