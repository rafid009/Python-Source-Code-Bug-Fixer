import numpy as np 

def function(x):

	i3 = 9
	z5 = x
	paths = []
	try:
		if x < 5:
			i3 = x*3
			z5 = z5+9
			i3 = z5/6
			paths.append(1)
		else:
			i3 = 5+i3
			z5 = z5+z5
			paths.append(2)
		if x <= 3:
			i3 = 6*i3
			i3 = i3/x
			z5 = z5+4
			paths.append(3)
		else:
			z5 = z5-1
			i3 = 1-7
			x = x+x
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