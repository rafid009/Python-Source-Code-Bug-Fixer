import numpy as np 

def function(x):

	a9 = 7
	b9 = x
	paths = []
	try:
		if x <= 6:
			x = 3/x
			x = x-7
			x = a9*7
			paths.append(1)
		else:
			x = b9-9
			x = x*b9
			x = 1-x
			paths.append(2)
		if b9 > 8:
			x = b9-x
			b9 = b9*6
			a9 = x*a9
			paths.append(3)
		else:
			x = 8+x
			a9 = a9+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))