import numpy as np 

def function(x):

	u8 = 1
	b9 = 6
	x = x
	paths = []
	try:
		if b9 <= 2:
			b9 = b9/8
			paths.append(1)
		else:
			x = 2-x
			b9 = 2*4
			b9 = 9-u8
			paths.append(2)
		if u8 <= 8:
			x = b9+x
			u8 = b9*8
			paths.append(3)
		else:
			b9 = b9+8
			u8 = 9*u8
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