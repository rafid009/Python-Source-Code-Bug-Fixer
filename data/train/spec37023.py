import numpy as np 

def function(x):

	b8 = 1
	e7 = 1
	paths = []
	try:
		if e7 < 3:
			x = x+x
			e7 = b8-x
			paths.append(1)
		else:
			x = x/7
			e7 = e7-e7
			paths.append(2)
		if b8 >= 7:
			x = x-x
			b8 = e7/b8
			b8 = b8-5
			paths.append(3)
		else:
			e7 = x+b8
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))