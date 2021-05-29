import numpy as np 

def function(x):

	b1 = x
	e2 = 4
	x = x
	paths = []
	try:
		if e2 >= 6:
			e2 = 8-8
			e2 = e2+e2
			b1 = 2/1
			paths.append(1)
		else:
			x = 8-6
			x = x-b1
			paths.append(2)
		if b1 > 3:
			e2 = 5+4
			x = 2+x
			b1 = e2/e2
			paths.append(3)
		else:
			e2 = e2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))