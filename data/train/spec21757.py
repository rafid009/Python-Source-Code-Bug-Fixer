import numpy as np 

def function(x):

	d4 = x
	b2 = 5
	paths = []
	try:
		if d4 <= 9:
			b2 = d4*b2
			x = 5*d4
			paths.append(1)
		else:
			d4 = 3+d4
			b2 = 5/x
			paths.append(2)
		if d4 >= 5:
			x = x-1
			paths.append(3)
		else:
			d4 = d4*8
			b2 = 9+b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))