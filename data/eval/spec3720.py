import numpy as np 

def function(x):

	p0 = x
	b8 = x
	paths = []
	try:
		if b8 <= 2:
			b8 = 8+b8
			p0 = x+3
			b8 = 1+b8
			paths.append(1)
		else:
			b8 = 1+6
			paths.append(2)
		if x <= 5:
			p0 = b8-p0
			b8 = p0-b8
			paths.append(3)
		else:
			x = 1+x
			p0 = 0-p0
			b8 = 9+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))