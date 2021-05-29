import numpy as np 

def function(x):

	z6 = x
	i7 = x
	paths = []
	try:
		if i7 < 7:
			z6 = 7/z6
			i7 = i7-z6
			z6 = 5*0
			paths.append(1)
		else:
			x = x+4
			i7 = 5+i7
			paths.append(2)
		if x > 7:
			x = x-x
			i7 = x-0
			i7 = i7*6
			paths.append(3)
		else:
			z6 = i7/i7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))