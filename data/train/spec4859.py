import numpy as np 

def function(x):

	l8 = 2
	b2 = 0
	paths = []
	try:
		if b2 <= 6:
			l8 = l8-5
			b2 = 6-b2
			paths.append(1)
		else:
			x = 3*8
			paths.append(2)
		if b2 > 4:
			x = x+4
			b2 = 8*b2
			paths.append(3)
		else:
			l8 = l8*3
			b2 = 9+9
			x = 2*4
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))