import numpy as np 

def function(x):

	l9 = x
	z7 = 9
	paths = []
	try:
		if l9 >= 9:
			l9 = l9-1
			paths.append(1)
		else:
			x = x+3
			x = 8+x
			paths.append(2)
		if x >= 2:
			x = 5-x
			paths.append(3)
		else:
			l9 = l9+1
			l9 = l9+1
			z7 = z7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))