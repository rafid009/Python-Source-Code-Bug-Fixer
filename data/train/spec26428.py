import numpy as np 

def function(x):

	b5 = 9
	e0 = x
	paths = []
	try:
		if e0 < 4:
			x = x-1
			b5 = e0*b5
			paths.append(1)
		else:
			e0 = e0/x
			e0 = 0/1
			paths.append(2)
		if b5 < 2:
			e0 = 2-e0
			paths.append(3)
		else:
			b5 = x/b5
			b5 = 2/b5
			e0 = 1+e0
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))