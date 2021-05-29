import numpy as np 

def function(x):

	z0 = x
	i0 = 5
	paths = []
	try:
		if i0 <= 2:
			i0 = 5+8
			x = x-8
			x = x/8
			paths.append(1)
		else:
			i0 = 8*i0
			x = x*7
			i0 = 7+3
			paths.append(2)
		if i0 < 4:
			x = x/i0
			i0 = i0-x
			paths.append(3)
		else:
			z0 = z0/9
			z0 = i0+6
			i0 = i0+x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))