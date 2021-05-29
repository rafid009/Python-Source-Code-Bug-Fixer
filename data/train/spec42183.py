import numpy as np 

def function(x):

	b8 = x
	b5 = 2
	paths = []
	try:
		if x >= 9:
			b8 = b8*4
			paths.append(1)
		else:
			x = x-b5
			paths.append(2)
		if b8 >= 7:
			b8 = 3-1
			b5 = b8*3
			paths.append(3)
		else:
			b5 = b8*2
			b5 = b5+0
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