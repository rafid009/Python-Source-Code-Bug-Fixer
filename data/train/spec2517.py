import numpy as np 

def function(x):

	z5 = x
	i3 = 0
	paths = []
	try:
		if i3 < 1:
			i3 = x/3
			z5 = 1/z5
			x = 7+x
			paths.append(1)
		else:
			i3 = i3*6
			z5 = i3-x
			z5 = z5*6
			paths.append(2)
		if i3 > 4:
			x = x-4
			i3 = 4*i3
			x = x*x
			paths.append(3)
		else:
			i3 = 3/i3
			z5 = z5-z5
			i3 = i3+7
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))