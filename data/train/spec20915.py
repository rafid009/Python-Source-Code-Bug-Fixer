import numpy as np 

def function(x):

	l4 = 7
	b4 = 3
	x = x
	paths = []
	try:
		if b4 <= 6:
			x = 9/x
			b4 = b4-4
			paths.append(1)
		else:
			b4 = b4/x
			paths.append(2)
		if x >= 0:
			x = x+6
			x = 6-4
			l4 = 0-0
			paths.append(3)
		else:
			x = 4-x
			l4 = l4/2
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