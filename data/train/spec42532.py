import numpy as np 

def function(x):

	n4 = x
	b8 = x
	x = x
	paths = []
	try:
		if b8 <= 7:
			b8 = x-5
			paths.append(1)
		else:
			b8 = b8*4
			n4 = n4/n4
			n4 = n4+5
			paths.append(2)
		if n4 >= 7:
			n4 = 6*n4
			b8 = b8*9
			x = x-b8
			paths.append(3)
		else:
			n4 = b8/n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		b8 = n4**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))