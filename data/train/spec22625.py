import numpy as np 

def function(x):

	z4 = 4
	f4 = 5
	paths = []
	try:
		if x < 0:
			f4 = f4*6
			x = 6*8
			paths.append(1)
		else:
			x = 6/6
			paths.append(2)
		if x <= 7:
			f4 = f4+f4
			z4 = z4+5
			f4 = 0/f4
			paths.append(3)
		else:
			z4 = z4/z4
			f4 = f4-x
			z4 = z4/9
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))