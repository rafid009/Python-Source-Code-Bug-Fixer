import numpy as np 

def function(x):

	e4 = x
	b9 = x
	paths = []
	try:
		if b9 >= 8:
			e4 = e4/5
			x = x+8
			paths.append(1)
		else:
			e4 = e4+6
			b9 = b9-9
			paths.append(2)
		if x >= 4:
			b9 = 0*e4
			paths.append(3)
		else:
			x = 2/8
			x = e4+b9
			b9 = 7*b9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		b9 = e4**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))