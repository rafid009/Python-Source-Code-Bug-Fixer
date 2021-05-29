import numpy as np 

def function(x):

	b8 = x
	e4 = x
	paths = []
	try:
		if e4 >= 7:
			b8 = e4+b8
			paths.append(1)
		else:
			b8 = 3-3
			x = b8+3
			b8 = e4*3
			paths.append(2)
		if b8 < 4:
			e4 = x-4
			paths.append(3)
		else:
			b8 = b8*e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		x = e4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))