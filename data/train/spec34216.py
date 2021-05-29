import numpy as np 

def function(x):

	e2 = 6
	b4 = x
	paths = []
	try:
		if b4 >= 5:
			b4 = b4/b4
			e2 = e2-4
			b4 = 4+e2
			paths.append(1)
		else:
			b4 = 3*2
			paths.append(2)
		if b4 < 3:
			x = 9-x
			e2 = e2*4
			paths.append(3)
		else:
			e2 = 6*x
			x = x-2
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