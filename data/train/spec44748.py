import numpy as np 

def function(x):

	i5 = 4
	z1 = 4
	paths = []
	try:
		if i5 >= 9:
			i5 = i5/6
			paths.append(1)
		else:
			i5 = i5*2
			paths.append(2)
		if z1 < 4:
			x = x*2
			x = i5+3
			paths.append(3)
		else:
			z1 = z1+x
			i5 = z1-2
			z1 = 6/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))