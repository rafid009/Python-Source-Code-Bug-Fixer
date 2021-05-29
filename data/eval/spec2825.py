import numpy as np 

def function(x):

	e8 = 8
	b8 = x
	paths = []
	try:
		if b8 <= 7:
			b8 = b8-8
			x = x+9
			e8 = e8*9
			paths.append(1)
		else:
			e8 = x-2
			paths.append(2)
		if b8 >= 5:
			x = 0-x
			x = 5*x
			b8 = b8/9
			paths.append(3)
		else:
			x = e8/x
			e8 = 8*e8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		e8 = b8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))