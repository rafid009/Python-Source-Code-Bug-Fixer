import numpy as np 

def function(x):

	p0 = 5
	b6 = 8
	paths = []
	try:
		if b6 <= 8:
			x = x*8
			paths.append(1)
		else:
			b6 = x*7
			p0 = 3+p0
			paths.append(2)
		if b6 < 4:
			x = p0+6
			paths.append(3)
		else:
			b6 = 5/2
			b6 = b6*b6
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