import numpy as np 

def function(x):

	b5 = 4
	x8 = x
	x = x
	paths = []
	try:
		if x > 4:
			x = 0-x
			x8 = 6-b5
			x = 8-x
			paths.append(1)
		else:
			b5 = 0*5
			b5 = 8*9
			x = x/2
			paths.append(2)
		if x < 4:
			b5 = 2*7
			b5 = b5+6
			x8 = 8+x8
			paths.append(3)
		else:
			x8 = b5/x8
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))