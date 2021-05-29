import numpy as np 

def function(x):

	b7 = 8
	e3 = 0
	paths = []
	try:
		if e3 < 4:
			x = x/6
			b7 = 1-b7
			paths.append(1)
		else:
			b7 = b7*6
			b7 = 6/b7
			e3 = e3/1
			paths.append(2)
		if b7 < 0:
			e3 = e3*7
			x = x/x
			paths.append(3)
		else:
			b7 = 2-6
			x = 8/x
			x = 4*6
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