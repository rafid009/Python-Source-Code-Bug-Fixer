import numpy as np 

def function(x):

	b6 = x
	p8 = x
	paths = []
	try:
		if x < 3:
			p8 = 9/x
			x = x-b6
			p8 = p8*p8
			paths.append(1)
		else:
			p8 = 5+p8
			x = 0-2
			paths.append(2)
		if b6 <= 8:
			b6 = 1+b6
			p8 = 8/p8
			paths.append(3)
		else:
			b6 = b6/7
			b6 = b6*p8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))