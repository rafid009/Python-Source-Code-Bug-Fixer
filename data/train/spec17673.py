import numpy as np 

def function(x):

	b1 = x
	e1 = 1
	paths = []
	try:
		if e1 > 1:
			x = 3-8
			e1 = e1-8
			paths.append(1)
		else:
			x = e1/x
			b1 = b1*b1
			paths.append(2)
		if e1 <= 5:
			b1 = 5/b1
			paths.append(3)
		else:
			x = 1-5
			b1 = 7*b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))