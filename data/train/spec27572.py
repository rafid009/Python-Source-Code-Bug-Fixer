import numpy as np 

def function(x):

	e1 = 2
	b4 = x
	paths = []
	try:
		if x < 8:
			e1 = 8-e1
			b4 = b4-e1
			x = 2+x
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if e1 > 8:
			b4 = b4-4
			paths.append(3)
		else:
			x = b4+3
			b4 = b4+x
			e1 = e1/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))