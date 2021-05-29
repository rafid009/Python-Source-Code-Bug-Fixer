import numpy as np 

def function(x):

	i3 = 1
	z4 = x
	paths = []
	try:
		if i3 < 8:
			z4 = i3-x
			paths.append(1)
		else:
			i3 = z4/7
			paths.append(2)
		if x > 0:
			i3 = z4-i3
			paths.append(3)
		else:
			i3 = i3-x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))