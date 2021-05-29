import numpy as np 

def function(x):

	b4 = 7
	r3 = 5
	paths = []
	try:
		if b4 <= 0:
			b4 = b4*4
			b4 = 2/b4
			paths.append(1)
		else:
			b4 = 3/b4
			b4 = b4+0
			paths.append(2)
		if x >= 6:
			r3 = 9+r3
			r3 = 7-b4
			paths.append(3)
		else:
			x = x*2
			r3 = 8+r3
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