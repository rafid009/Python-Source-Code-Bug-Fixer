import numpy as np 

def function(x):

	b6 = x
	e2 = x
	paths = []
	try:
		if x <= 6:
			b6 = b6/b6
			paths.append(1)
		else:
			x = 9+x
			x = x+7
			e2 = 6-1
			paths.append(2)
		if b6 < 6:
			x = 8*x
			b6 = b6-e2
			x = x+e2
			paths.append(3)
		else:
			b6 = 0-b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))