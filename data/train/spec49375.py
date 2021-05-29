import numpy as np 

def function(x):

	b4 = x
	b8 = 0
	paths = []
	try:
		if x >= 8:
			x = x+7
			paths.append(1)
		else:
			b8 = 5-b8
			paths.append(2)
		if x <= 8:
			x = 8+x
			paths.append(3)
		else:
			b8 = 8/x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b8 = b4**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))