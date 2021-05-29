import numpy as np 

def function(x):

	b4 = 6
	b7 = x
	paths = []
	try:
		if b4 <= 9:
			x = 7-5
			paths.append(1)
		else:
			b4 = b4/7
			b4 = b4*8
			paths.append(2)
		if b7 <= 4:
			b4 = b7+8
			b4 = 1-b4
			x = 9*x
			paths.append(3)
		else:
			x = 4+0
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))