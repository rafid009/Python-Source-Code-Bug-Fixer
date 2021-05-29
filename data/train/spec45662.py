import numpy as np 

def function(x):

	z6 = x
	i5 = x
	paths = []
	try:
		if i5 >= 2:
			x = z6*4
			i5 = i5/i5
			paths.append(1)
		else:
			x = x/z6
			i5 = 6*i5
			paths.append(2)
		if z6 >= 5:
			i5 = 5-i5
			x = 6/7
			paths.append(3)
		else:
			z6 = z6+9
			i5 = 0-i5
			z6 = z6+i5
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))