import numpy as np 

def function(x):

	b7 = 9
	b4 = x
	paths = []
	try:
		if x <= 6:
			b7 = 5*b4
			x = 8/b7
			paths.append(1)
		else:
			b7 = 6+6
			b7 = b4-6
			b4 = b4+4
			paths.append(2)
		if x >= 8:
			x = 2-x
			b4 = 0-9
			paths.append(3)
		else:
			x = x/x
			b4 = b4/5
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b7 = b4**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))