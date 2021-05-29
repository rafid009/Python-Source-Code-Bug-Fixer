import numpy as np 

def function(x):

	b5 = 7
	p7 = 2
	paths = []
	try:
		if p7 > 2:
			p7 = 8/p7
			paths.append(1)
		else:
			x = 0-8
			x = x-p7
			b5 = 8-8
			paths.append(2)
		if b5 <= 6:
			b5 = 6-b5
			p7 = p7+8
			x = x-p7
			paths.append(3)
		else:
			p7 = p7+b5
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