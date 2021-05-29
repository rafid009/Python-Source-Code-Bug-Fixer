import numpy as np 

def function(x):

	d7 = x
	b8 = 1
	paths = []
	try:
		if x < 2:
			x = 7/x
			paths.append(1)
		else:
			b8 = b8*d7
			paths.append(2)
		if d7 <= 1:
			b8 = b8/2
			paths.append(3)
		else:
			b8 = x*d7
			b8 = 7/b8
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))