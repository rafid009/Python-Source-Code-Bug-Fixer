import numpy as np 

def function(x):

	b8 = 4
	a9 = 1
	paths = []
	try:
		if x <= 8:
			x = 0+x
			paths.append(1)
		else:
			b8 = b8+x
			paths.append(2)
		if a9 > 5:
			b8 = b8+1
			paths.append(3)
		else:
			b8 = a9*a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))