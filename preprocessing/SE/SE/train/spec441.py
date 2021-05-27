import numpy as np 

def function(x):

	p8 = x
	b0 = 1
	paths = []
	try:
		if b0 > 4:
			x = x-p8
			x = x+p8
			paths.append(1)
		else:
			p8 = p8+3
			p8 = p8/4
			paths.append(2)
		if b0 > 5:
			b0 = 3*b0
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))