import numpy as np 

def function(x):

	e1 = 4
	b6 = 5
	paths = []
	try:
		if e1 < 5:
			e1 = 6*5
			e1 = 8*7
			b6 = e1/e1
			paths.append(1)
		else:
			b6 = 6/2
			b6 = 6/2
			e1 = 0-e1
			paths.append(2)
		if b6 >= 7:
			e1 = e1+2
			x = x-2
			paths.append(3)
		else:
			e1 = e1+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))