import numpy as np 

def function(x):

	a6 = x
	b9 = x
	paths = []
	try:
		if b9 >= 0:
			x = 1+a6
			b9 = 5/3
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if a6 < 1:
			x = x/3
			b9 = b9+7
			paths.append(3)
		else:
			a6 = 7*9
			b9 = b9*8
			b9 = b9+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))