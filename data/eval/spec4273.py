import numpy as np 

def function(x):

	b0 = 7
	e6 = x
	paths = []
	try:
		if e6 > 0:
			b0 = e6/b0
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if e6 >= 3:
			b0 = b0/b0
			x = e6-e6
			e6 = e6-b0
			paths.append(3)
		else:
			x = x+4
			b0 = b0-e6
			b0 = 7-9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		e6 = b0**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))