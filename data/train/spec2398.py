import numpy as np 

def function(x):

	z4 = x
	i7 = 1
	paths = []
	try:
		if i7 > 1:
			z4 = z4*i7
			x = z4/z4
			i7 = 5/9
			paths.append(1)
		else:
			i7 = z4*x
			z4 = 6-x
			i7 = i7*i7
			paths.append(2)
		if x < 2:
			i7 = i7+i7
			z4 = z4/8
			paths.append(3)
		else:
			i7 = 4/4
			i7 = i7+z4
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