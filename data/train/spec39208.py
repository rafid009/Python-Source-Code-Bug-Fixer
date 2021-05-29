import numpy as np 

def function(x):

	e8 = 4
	b4 = 6
	paths = []
	try:
		if b4 < 0:
			x = 1-0
			x = 8+x
			x = 1-x
			paths.append(1)
		else:
			e8 = x*8
			e8 = e8-x
			paths.append(2)
		if e8 > 5:
			b4 = 7/b4
			x = e8/e8
			paths.append(3)
		else:
			b4 = b4*e8
			b4 = b4+e8
			e8 = e8*4
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