import numpy as np 

def function(x):

	b2 = x
	a3 = x
	x = x
	paths = []
	try:
		if x <= 7:
			x = x-b2
			b2 = b2-9
			b2 = 0-3
			paths.append(1)
		else:
			a3 = a3+9
			a3 = b2/a3
			x = x-8
			paths.append(2)
		if x > 6:
			b2 = 3+b2
			paths.append(3)
		else:
			b2 = a3-3
			a3 = a3-a3
			a3 = a3-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))