import numpy as np 

def function(x):

	b8 = 5
	b5 = 7
	paths = []
	try:
		if b5 > 8:
			x = 9*x
			paths.append(1)
		else:
			b8 = 7-b8
			x = 6-b5
			paths.append(2)
		if b8 <= 3:
			b5 = 3/1
			b5 = 6+b5
			b5 = b5/2
			paths.append(3)
		else:
			b8 = 7/b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))