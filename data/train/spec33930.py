import numpy as np 

def function(x):

	e5 = x
	b4 = x
	paths = []
	try:
		if b4 > 2:
			b4 = x-2
			x = 1/x
			paths.append(1)
		else:
			x = x-7
			b4 = b4+b4
			paths.append(2)
		if e5 <= 6:
			x = 0+9
			e5 = 6-e5
			b4 = b4+6
			paths.append(3)
		else:
			e5 = 3-b4
			b4 = b4+e5
			x = x-e5
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		e5 = b4**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))