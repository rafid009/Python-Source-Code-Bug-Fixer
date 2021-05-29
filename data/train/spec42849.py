import numpy as np 

def function(x):

	p3 = x
	b7 = x
	paths = []
	try:
		if x <= 7:
			b7 = b7/p3
			p3 = 4*p3
			x = b7-x
			paths.append(1)
		else:
			p3 = 6/p3
			paths.append(2)
		if x <= 2:
			x = 0-5
			paths.append(3)
		else:
			x = x/8
			p3 = p3*8
			x = p3*b7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))