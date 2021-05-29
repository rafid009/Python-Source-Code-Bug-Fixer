import numpy as np 

def function(x):

	e8 = x
	b5 = 8
	paths = []
	try:
		if x >= 8:
			b5 = x-9
			paths.append(1)
		else:
			b5 = b5/3
			paths.append(2)
		if b5 > 4:
			e8 = 8+e8
			paths.append(3)
		else:
			b5 = b5*7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))