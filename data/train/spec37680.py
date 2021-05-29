import numpy as np 

def function(x):

	b8 = 7
	b5 = 7
	paths = []
	try:
		if b5 >= 0:
			b8 = b5+5
			paths.append(1)
		else:
			b8 = b8-x
			paths.append(2)
		if b5 < 2:
			x = b5/x
			b8 = b8/6
			paths.append(3)
		else:
			b8 = x/b5
			b5 = b5*b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))