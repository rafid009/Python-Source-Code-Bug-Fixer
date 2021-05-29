import numpy as np 

def function(x):

	e8 = 6
	b4 = x
	paths = []
	try:
		if b4 <= 4:
			b4 = b4+5
			e8 = 0+e8
			x = x*x
			paths.append(1)
		else:
			e8 = e8*e8
			paths.append(2)
		if x >= 1:
			b4 = 7/b4
			e8 = e8/7
			paths.append(3)
		else:
			e8 = 2-e8
			b4 = 7-b4
			b4 = 9*b4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))