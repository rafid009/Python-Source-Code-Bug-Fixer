import numpy as np 

def function(x):

	e4 = 5
	b4 = 6
	paths = []
	try:
		if b4 <= 6:
			b4 = x+b4
			paths.append(1)
		else:
			b4 = b4/x
			e4 = 5/e4
			x = 3-x
			paths.append(2)
		if b4 > 4:
			e4 = e4*3
			b4 = b4/1
			paths.append(3)
		else:
			b4 = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))