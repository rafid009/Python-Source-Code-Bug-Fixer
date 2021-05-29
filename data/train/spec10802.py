import numpy as np 

def function(x):

	b6 = 4
	a6 = 0
	paths = []
	try:
		if b6 >= 2:
			x = x-1
			b6 = b6/7
			x = 2/x
			paths.append(1)
		else:
			b6 = 8+b6
			b6 = 9/a6
			paths.append(2)
		if b6 <= 0:
			x = x+9
			a6 = a6-x
			paths.append(3)
		else:
			b6 = b6-8
			a6 = 1-a6
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