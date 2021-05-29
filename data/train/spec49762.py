import numpy as np 

def function(x):

	b3 = x
	b5 = x
	paths = []
	try:
		if b3 < 3:
			b5 = 8-b5
			paths.append(1)
		else:
			b3 = 9*7
			b5 = b5/2
			paths.append(2)
		if b5 >= 8:
			x = 2/8
			x = b3-2
			paths.append(3)
		else:
			x = 1-x
			x = x/b5
			x = x*9
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))