import numpy as np 

def function(x):

	e7 = 7
	b7 = x
	paths = []
	try:
		if e7 >= 6:
			e7 = 4-e7
			paths.append(1)
		else:
			e7 = 3+e7
			paths.append(2)
		if x >= 0:
			b7 = 5*1
			b7 = b7*3
			paths.append(3)
		else:
			x = x/1
			e7 = e7-b7
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