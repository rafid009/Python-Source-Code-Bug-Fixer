import numpy as np 

def function(x):

	q4 = 5
	b8 = x
	paths = []
	try:
		if x < 3:
			x = 0-7
			paths.append(1)
		else:
			x = 0+q4
			paths.append(2)
		if q4 <= 4:
			q4 = 2+4
			b8 = 1*b8
			b8 = 8/b8
			paths.append(3)
		else:
			x = x+2
			b8 = b8-6
			b8 = x/b8
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