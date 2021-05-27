import numpy as np 

def function(x):

	p4 = 3
	b8 = x
	paths = []
	try:
		if x >= 6:
			x = p4-0
			p4 = p4+5
			x = 0-x
			paths.append(1)
		else:
			p4 = 4*p4
			paths.append(2)
		if b8 < 2:
			b8 = b8+b8
			b8 = 3+3
			paths.append(3)
		else:
			p4 = p4*9
			x = x-0
			x = 8/b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))