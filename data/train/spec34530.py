import numpy as np 

def function(x):

	z0 = 8
	i6 = 4
	paths = []
	try:
		if i6 >= 7:
			i6 = x*5
			z0 = z0*4
			x = x*1
			paths.append(1)
		else:
			i6 = i6*3
			x = x+9
			paths.append(2)
		if x > 3:
			z0 = x*7
			i6 = z0*2
			x = 4+3
			paths.append(3)
		else:
			i6 = i6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))