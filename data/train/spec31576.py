import numpy as np 

def function(x):

	n4 = 4
	b4 = 2
	paths = []
	try:
		if b4 > 2:
			x = x-4
			x = 1*8
			paths.append(1)
		else:
			b4 = 3-b4
			paths.append(2)
		if b4 <= 4:
			b4 = b4-4
			x = x*4
			n4 = 4*n4
			paths.append(3)
		else:
			x = 9*3
			b4 = x*b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))