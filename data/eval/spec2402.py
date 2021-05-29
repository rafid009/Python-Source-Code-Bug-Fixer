import numpy as np 

def function(x):

	b4 = 2
	a3 = x
	paths = []
	try:
		if b4 > 0:
			b4 = 5-b4
			a3 = 3/7
			paths.append(1)
		else:
			a3 = 6/x
			b4 = a3/b4
			paths.append(2)
		if x < 6:
			b4 = b4-2
			a3 = b4-9
			paths.append(3)
		else:
			a3 = 0/a3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))