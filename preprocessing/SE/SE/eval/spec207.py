import numpy as np 

def function(x):

	b4 = 8
	e8 = x
	paths = []
	try:
		if x >= 2:
			x = x/5
			x = b4/x
			paths.append(1)
		else:
			b4 = b4/e8
			e8 = e8+e8
			e8 = e8+8
			paths.append(2)
		if x >= 3:
			b4 = b4+x
			x = x/9
			paths.append(3)
		else:
			b4 = 7/b4
			b4 = x*7
			x = x*b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		e8 = b4**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))