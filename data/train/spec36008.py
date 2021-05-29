import numpy as np 

def function(x):

	z6 = 1
	i1 = x
	paths = []
	try:
		if i1 <= 7:
			i1 = i1*x
			paths.append(1)
		else:
			x = 5-x
			z6 = z6*z6
			z6 = z6/8
			paths.append(2)
		if i1 >= 4:
			i1 = 1-i1
			i1 = x+x
			paths.append(3)
		else:
			z6 = 3+z6
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))