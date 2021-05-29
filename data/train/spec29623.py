import numpy as np 

def function(x):

	i6 = 9
	z6 = 3
	paths = []
	try:
		if z6 > 5:
			z6 = 7/6
			x = 4/z6
			paths.append(1)
		else:
			i6 = x/z6
			paths.append(2)
		if x >= 1:
			z6 = z6+7
			z6 = 9-0
			z6 = 1*6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))