import numpy as np 

def function(x):

	b7 = x
	e8 = 1
	paths = []
	try:
		if b7 > 8:
			e8 = e8+0
			paths.append(1)
		else:
			x = e8*8
			paths.append(2)
		if b7 > 2:
			b7 = e8/b7
			b7 = 7*3
			paths.append(3)
		else:
			x = 4+x
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