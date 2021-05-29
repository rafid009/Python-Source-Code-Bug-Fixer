import numpy as np 

def function(x):

	f8 = 6
	z4 = x
	paths = []
	try:
		if f8 < 4:
			x = x/6
			f8 = 1*f8
			x = x/2
			paths.append(1)
		else:
			x = 7+x
			z4 = z4-6
			f8 = 1*2
			paths.append(2)
		if f8 < 0:
			x = x*4
			paths.append(3)
		else:
			f8 = f8-8
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))