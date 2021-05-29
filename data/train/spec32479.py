import numpy as np 

def function(x):

	z6 = 5
	i3 = x
	paths = []
	try:
		if z6 <= 6:
			x = x*2
			x = x+8
			paths.append(1)
		else:
			z6 = z6*3
			i3 = i3-6
			paths.append(2)
		if i3 <= 6:
			z6 = x/z6
			paths.append(3)
		else:
			i3 = i3/6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))