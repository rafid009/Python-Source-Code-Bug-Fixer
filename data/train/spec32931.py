import numpy as np 

def function(x):

	e4 = 3
	b7 = 0
	paths = []
	try:
		if e4 > 5:
			b7 = b7*x
			paths.append(1)
		else:
			x = x*3
			e4 = 7-4
			b7 = x-4
			paths.append(2)
		if e4 < 5:
			b7 = b7*x
			e4 = e4-b7
			paths.append(3)
		else:
			x = 0+5
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		b7 = e4**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))