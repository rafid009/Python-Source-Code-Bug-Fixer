import numpy as np 

def function(x):

	e6 = x
	b1 = 8
	paths = []
	try:
		if e6 <= 3:
			e6 = x/9
			paths.append(1)
		else:
			e6 = 4+8
			b1 = b1/b1
			paths.append(2)
		if e6 <= 5:
			b1 = b1+5
			x = b1+x
			b1 = 2+6
			paths.append(3)
		else:
			b1 = 1+b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))