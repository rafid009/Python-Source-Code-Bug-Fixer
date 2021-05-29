import numpy as np 

def function(x):

	e8 = 1
	b2 = x
	x = 7
	paths = []
	try:
		if b2 <= 2:
			e8 = x+e8
			paths.append(1)
		else:
			e8 = 1/b2
			x = x-0
			b2 = b2*b2
			paths.append(2)
		if e8 <= 0:
			x = x*7
			paths.append(3)
		else:
			b2 = 8/b2
			b2 = b2+b2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))