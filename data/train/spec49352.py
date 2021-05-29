import numpy as np 

def function(x):

	z0 = x
	i6 = 2
	paths = []
	try:
		if x > 8:
			i6 = i6/z0
			paths.append(1)
		else:
			i6 = i6*z0
			i6 = 5+i6
			paths.append(2)
		if i6 >= 7:
			z0 = 2/4
			i6 = 7*i6
			x = x/2
			paths.append(3)
		else:
			z0 = z0+1
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