import numpy as np 

def function(x):

	b2 = x
	b4 = 3
	paths = []
	try:
		if b4 >= 7:
			b2 = 5/b2
			b2 = 5-b2
			b4 = b4+b4
			paths.append(1)
		else:
			x = 4-b4
			paths.append(2)
		if b4 <= 6:
			x = x-5
			paths.append(3)
		else:
			x = 8+4
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))