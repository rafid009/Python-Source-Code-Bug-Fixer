import numpy as np 

def function(x):

	e9 = 4
	b5 = x
	x = x
	paths = []
	try:
		if x >= 3:
			b5 = b5/8
			paths.append(1)
		else:
			x = 4-7
			paths.append(2)
		if b5 < 4:
			e9 = e9/5
			paths.append(3)
		else:
			e9 = 7*8
			x = e9/b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))