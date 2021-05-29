import numpy as np 

def function(x):

	e3 = 8
	b8 = 3
	paths = []
	try:
		if b8 >= 9:
			e3 = e3/1
			paths.append(1)
		else:
			b8 = b8+4
			b8 = b8-b8
			e3 = e3-6
			paths.append(2)
		if b8 < 0:
			e3 = b8/b8
			b8 = 1*b8
			e3 = 6-e3
			paths.append(3)
		else:
			x = 5-7
			b8 = e3*x
			b8 = 3+b8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))