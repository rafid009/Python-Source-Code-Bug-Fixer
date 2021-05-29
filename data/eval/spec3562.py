import numpy as np 

def function(x):

	r6 = 6
	b4 = x
	paths = []
	try:
		if x <= 2:
			x = 9+0
			paths.append(1)
		else:
			b4 = x-x
			paths.append(2)
		if r6 <= 1:
			x = b4+3
			paths.append(3)
		else:
			x = 8-x
			r6 = 8+r6
			b4 = 8-3
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