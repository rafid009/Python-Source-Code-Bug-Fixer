import numpy as np 

def function(x):

	b8 = x
	a4 = 8
	paths = []
	try:
		if b8 <= 0:
			b8 = b8+6
			a4 = 7+x
			paths.append(1)
		else:
			a4 = 5/a4
			paths.append(2)
		if b8 <= 0:
			x = 0+x
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))